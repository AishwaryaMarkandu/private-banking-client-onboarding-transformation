"""
Private Banking Client Onboarding Transformation

I built this project as a consulting-style case study for a hypothetical
Luxembourg private bank. All operational data is synthetic and reproducible.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SEED = 42
N_CASES = 6000
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def generate_cases(seed=SEED, n=N_CASES):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "onboarding_id": [f"PB-{i:06d}" for i in range(1, n + 1)],
        "received_date": pd.to_datetime(rng.choice(pd.date_range("2025-01-01", "2025-12-31"), n)),
        "client_segment": rng.choice(["HNWI","UHNWI","Family Office","Entrepreneur"], n, p=[.48,.24,.16,.12]),
        "risk_tier": rng.choice(["Low","Medium","High"], n, p=[.38,.47,.15]),
        "channel": rng.choice(["Relationship Manager","Digital Referral","Partner / Intermediary"], n, p=[.56,.26,.18]),
        "client_region": rng.choice(["Luxembourg","France","Belgium","Germany","Switzerland","UK","Other"], n, p=[.16,.22,.14,.13,.12,.09,.14]),
        "client_type": rng.choice(["Individual","Corporate / Holding","Trust / Foundation"], n, p=[.56,.28,.16])
    })
    df["expected_documents"] = (
        6
        + df.client_type.map({"Individual":0,"Corporate / Holding":4,"Trust / Foundation":7})
        + df.risk_tier.map({"Low":0,"Medium":2,"High":5})
        + rng.poisson(1.4, n)
    ).astype(int)
    df["missing_document_events"] = np.clip(rng.poisson(
        .55 + df.risk_tier.map({"Low":.05,"Medium":.30,"High":.75}).to_numpy()
        + df.client_type.map({"Individual":0,"Corporate / Holding":.25,"Trust / Foundation":.45}).to_numpy(), n), 0, 7)
    df["manual_touchpoints"] = np.clip(np.round(
        2.5 + df.expected_documents*.42 + df.missing_document_events*.95
        + df.risk_tier.map({"Low":0,"Medium":1,"High":2}).to_numpy()
        + rng.normal(0,1,n)), 1, 18).astype(int)
    df["cycle_time_days"] = np.clip(np.round(
        7 + df.risk_tier.map({"Low":0,"Medium":3.5,"High":8}).to_numpy()
        + df.client_type.map({"Individual":0,"Corporate / Holding":3.5,"Trust / Foundation":6}).to_numpy()
        + df.missing_document_events*2.4 + df.manual_touchpoints*.55 + rng.normal(0,3,n)
        + df.channel.map({"Relationship Manager":1,"Digital Referral":-.7,"Partner / Intermediary":2}).to_numpy(), 1), 2, 75)
    df["sla_target_days"] = df.risk_tier.map({"Low":18,"Medium":25,"High":38}).astype(int)
    df["sla_breach"] = df.cycle_time_days > df.sla_target_days
    df["rework_events"] = np.clip(rng.poisson(.45 + df.missing_document_events*.28 + df.manual_touchpoints*.04, n), 0, 8)
    df["compliance_escalation"] = (
        (df.risk_tier.eq("High") & (rng.random(n) < .48))
        | (df.missing_document_events >= 4)
        | (df.rework_events >= 4)
    )
    df["screening_alerts"] = np.clip(rng.poisson(
        .08 + df.risk_tier.map({"Low":.02,"Medium":.08,"High":.28}).to_numpy()
        + df.client_type.map({"Individual":0,"Corporate / Holding":.03,"Trust / Foundation":.07}).to_numpy(), n), 0, 5)
    df["relationship_manager_hours"] = np.round(
        .8 + df.manual_touchpoints*.18 + df.rework_events*.35
        + df.compliance_escalation.astype(int)*.75 + rng.normal(0,.35,n), 1).clip(.5, 12)
    df["outcome"] = np.where(
        (df.cycle_time_days > 42) | (df.risk_tier.eq("High") & (df.screening_alerts >= 3)),
        rng.choice(["Withdrawn","Declined"], n, p=[.7,.3]),
        np.where(rng.random(n) < .055, "Withdrawn", "Onboarded")
    )
    df["month"] = df.received_date.dt.to_period("M").astype(str)
    return df

def build_step_summary(df):
    rng = np.random.default_rng(SEED)
    specs = [
        ("Initial data capture",1.0,.10,.08),("Document collection",3.2,.36,.42),
        ("KYC / identity verification",2.1,.28,.31),("Beneficial ownership review",2.8,.42,.35),
        ("Source of wealth / funds",3.7,.48,.39),("PEP / sanctions screening",1.4,.16,.12),
        ("Compliance assessment",2.9,.38,.27),("Acceptance approval",1.9,.22,.18),
        ("Account opening",1.4,.14,.10)
    ]
    rows=[]
    for name,base,mrate,rrate in specs:
        risk = df.risk_tier.map({"Low":0,"Medium":.55,"High":1.35}).to_numpy() if name in [
            "Beneficial ownership review","Source of wealth / funds","Compliance assessment"
        ] else df.risk_tier.map({"Low":0,"Medium":.25,"High":.55}).to_numpy()
        duration=np.clip(base+risk+rng.normal(0,.65,len(df)),.2,None)
        rows.append(pd.DataFrame({
            "step":name,
            "duration":duration,
            "manual":rng.random(len(df))<np.clip(mrate+df.manual_touchpoints.to_numpy()/70,0,.95),
            "rework":rng.random(len(df))<np.clip(rrate+df.rework_events.to_numpy()/35,0,.9)
        }))
    detail=pd.concat(rows,ignore_index=True)
    out=detail.groupby("step",as_index=False).agg(
        avg_duration_days=("duration","mean"),
        manual_touchpoint_rate=("manual","mean"),
        rework_rate=("rework","mean")
    )
    out["avg_duration_days"]=out.avg_duration_days.round(2)
    out["manual_touchpoint_rate"]=(out.manual_touchpoint_rate*100).round(1)
    out["rework_rate"]=(out.rework_rate*100).round(1)
    return out

def build_business_outputs(df):
    kpi=pd.DataFrame({
        "kpi":["Total onboarding cases","Onboarding completion rate","SLA compliance rate",
               "Average cycle time (days)","Median cycle time (days)","Average RM effort (hours)",
               "Cases with rework","High-risk client share"],
        "value":[len(df),df.outcome.eq("Onboarded").mean()*100,(~df.sla_breach).mean()*100,
                 df.cycle_time_days.mean(),df.cycle_time_days.median(),
                 df.relationship_manager_hours.mean(),(df.rework_events>0).mean()*100,
                 df.risk_tier.eq("High").mean()*100]
    })
    kpi["value"]=kpi.value.round(2)

    monthly=df.groupby("month").agg(
        cases=("onboarding_id","count"),avg_cycle_time_days=("cycle_time_days","mean"),
        sla_breach_rate=("sla_breach","mean"),avg_manual_touchpoints=("manual_touchpoints","mean"),
        avg_rm_hours=("relationship_manager_hours","mean")).reset_index()
    monthly["sla_breach_rate"]=(monthly.sla_breach_rate*100).round(2)
    monthly["avg_cycle_time_days"]=monthly.avg_cycle_time_days.round(2)
    monthly["avg_manual_touchpoints"]=monthly.avg_manual_touchpoints.round(2)
    monthly["avg_rm_hours"]=monthly.avg_rm_hours.round(2)

    opportunities=pd.DataFrame([
        ["Digital document intake & completeness validation",5,5,4,5,"Client Onboarding / Operations","0–6 months"],
        ["KYC workflow orchestration",5,4,5,4,"Operations / Compliance / Technology","3–9 months"],
        ["Risk-based onboarding routing",5,4,5,4,"Compliance / Operations","3–9 months"],
        ["RM onboarding cockpit",4,5,3,5,"Front Office / Operations","0–6 months"],
        ["Exception & SLA management dashboard",4,5,4,4,"Operations / PMO","0–3 months"],
        ["Reusable KYC evidence & document repository",4,3,4,5,"Operations / Technology","6–12 months"],
    ], columns=["opportunity","value","feasibility","risk_reduction","client_experience","owner","horizon"])
    opportunities["priority_score"]=(opportunities.value*.35+opportunities.feasibility*.20+
                                      opportunities.risk_reduction*.25+opportunities.client_experience*.20).round(2)
    opportunities["priority"]=pd.cut(opportunities.priority_score,[0,3,4,5.1],
                                     labels=["Explore","Prioritise","Accelerate"],include_lowest=True)

    business=pd.DataFrame([
        ["Average cycle time",df.cycle_time_days.mean(),df.cycle_time_days.mean()*.72,"days"],
        ["Relationship-manager effort",df.relationship_manager_hours.sum(),df.relationship_manager_hours.sum()*.78,"hours"],
        ["Rework reduction",0,35,"%"],
        ["SLA improvement",0,12,"percentage points"]
    ],columns=["metric","baseline","target","unit"]).round(2)

    roadmap=pd.DataFrame([
        ["0–3 months","Stabilise","Establish KPI baseline; implement exception dashboard; clarify ownership and SLAs.","Operations / PMO"],
        ["3–6 months","Simplify","Redesign document intake; introduce completeness validation; reduce avoidable hand-offs.","Operations / Compliance"],
        ["6–12 months","Orchestrate","Implement risk-based routing and workflow orchestration across KYC and approval steps.","Technology / Operations"],
        ["12–18 months","Scale","Deploy reusable evidence repository and RM onboarding cockpit; embed continuous improvement.","Technology / Front Office"],
        ["18+ months","Optimise","Evaluate advanced automation and AI-assisted document / case processing with appropriate controls.","Transformation Office"]
    ],columns=["phase","theme","key_actions","owner"])

    raci=pd.DataFrame([
        ["Relationship Manager","R","R","C","I","R"],["Client Onboarding Operations","A","R","R","R","C"],
        ["KYC / Compliance","C","A","R","R","C"],["Risk","I","C","A","C","I"],["Technology","C","C","C","A","R"]
    ],columns=["role","Client Intake","Document & KYC","Risk Assessment","Approval","Case Management"])
    return kpi,monthly,opportunities,business,roadmap,raci

def main():
    df=generate_cases()
    steps=build_step_summary(df)
    kpi,monthly,opportunities,business,roadmap,raci=build_business_outputs(df)

    df.to_csv(OUTPUT_DIR/"synthetic_onboarding_cases.csv",index=False)
    steps.to_csv(OUTPUT_DIR/"step_performance.csv",index=False)
    kpi.to_csv(OUTPUT_DIR/"kpi_summary.csv",index=False)
    monthly.to_csv(OUTPUT_DIR/"monthly_operational_kpis.csv",index=False)
    opportunities.to_csv(OUTPUT_DIR/"transformation_opportunities.csv",index=False)
    business.to_csv(OUTPUT_DIR/"business_case.csv",index=False)
    roadmap.to_csv(OUTPUT_DIR/"transformation_roadmap.csv",index=False)
    raci.to_csv(OUTPUT_DIR/"target_operating_model_raci.csv",index=False)

    plt.figure(figsize=(11,5))
    plt.plot(monthly.month,monthly.cases,marker="o")
    plt.title("Private Banking Onboarding Volume — Synthetic 2025 Scenario")
    plt.xlabel("Month"); plt.ylabel("Cases")
    plt.xticks(rotation=45,ha="right"); plt.tight_layout()
    plt.savefig(OUTPUT_DIR/"monthly_onboarding_volume.png",dpi=160); plt.close()

    plt.figure(figsize=(10,5.5))
    p=steps.sort_values("avg_duration_days")
    plt.barh(p.step,p.avg_duration_days)
    plt.title("Average Duration by Onboarding Step"); plt.xlabel("Average duration (days)")
    plt.tight_layout(); plt.savefig(OUTPUT_DIR/"step_duration.png",dpi=160); plt.close()

    plt.figure(figsize=(10,5.5))
    p=opportunities.sort_values("priority_score")
    plt.barh(p.opportunity,p.priority_score); plt.xlim(0,5)
    plt.title("Transformation Opportunity Prioritisation"); plt.xlabel("Priority score / 5")
    plt.tight_layout(); plt.savefig(OUTPUT_DIR/"transformation_opportunity_priority.png",dpi=160); plt.close()

    print(f"I analysed {len(df):,} synthetic onboarding cases.")
    print(f"Average cycle time: {df.cycle_time_days.mean():.1f} days")
    print(f"SLA compliance: {(~df.sla_breach).mean()*100:.1f}%")
    print("Outputs written to ./outputs")

if __name__=="__main__":
    main()
