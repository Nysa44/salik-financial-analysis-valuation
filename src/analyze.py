from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT, FIG = ROOT/"outputs", ROOT/"outputs"/"figures"
FIG.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(ROOT/"data"/"historical_financials.csv").sort_values("fiscal_year")
rev = pd.read_csv(ROOT/"data"/"revenue_breakdown.csv")

for metric in ["revenue_aed_m", "ebitda_aed_m", "net_profit_aed_m", "free_cash_flow_aed_m"]:
    df[metric.replace("_aed_m", "_growth_pct")] = df[metric].pct_change()*100
df["calculated_ebitda_margin_pct"] = df.ebitda_aed_m/df.revenue_aed_m*100
df["calculated_net_profit_margin_pct"] = df.net_profit_aed_m/df.revenue_aed_m*100
df["fcf_margin_pct"] = df.free_cash_flow_aed_m/df.revenue_aed_m*100
df.to_csv(OUT/"ratio_analysis.csv", index=False)

fig, ax = plt.subplots(figsize=(10,5.5))
for col, label in [("revenue_aed_m","Revenue"),("ebitda_aed_m","EBITDA"),("net_profit_aed_m","Net profit")]:
    ax.plot(df.fiscal_year, df[col]/1000, marker="o", linewidth=2, label=label)
ax.set_title("Salik — three-year financial performance")
ax.set_ylabel("AED billions")
ax.set_xticks(df.fiscal_year)
ax.grid(axis="y", alpha=.25)
ax.legend(frameon=False, ncols=3)
fig.tight_layout()
fig.savefig(FIG/"financial_performance.png", dpi=180)
plt.close(fig)

fig, ax = plt.subplots(figsize=(10,5.5))
plot = rev.sort_values("fy2025_aed_m")
ax.barh(plot.category, plot.fy2025_aed_m, label="FY2025")
ax.set_title("Revenue composition — FY2025")
ax.set_xlabel("AED millions")
ax.grid(axis="x", alpha=.25)
fig.tight_layout()
fig.savefig(FIG/"revenue_composition.png", dpi=180)
plt.close(fig)

latest, prior = df.iloc[-1], df.iloc[-2]
rev_growth = (latest.revenue_aed_m/prior.revenue_aed_m-1)*100
ebitda_growth = (latest.ebitda_aed_m/prior.ebitda_aed_m-1)*100
np_growth = (latest.net_profit_aed_m/prior.net_profit_aed_m-1)*100
trips_growth = (latest.revenue_generating_trips_m/prior.revenue_generating_trips_m-1)*100
report = f"""# Salik — Financial highlights

## FY2025 vs FY2024
- Revenue: **AED {latest.revenue_aed_m/1000:.3f}bn**, up **{rev_growth:.1f}%**.
- EBITDA: **AED {latest.ebitda_aed_m/1000:.3f}bn**, up **{ebitda_growth:.1f}%**.
- Net profit: **AED {latest.net_profit_aed_m/1000:.3f}bn**, up **{np_growth:.1f}%**.
- Revenue-generating trips: **{latest.revenue_generating_trips_m:.1f} million**, up **{trips_growth:.1f}%**.
- EBITDA margin: **{latest.ebitda_margin_pct:.1f}%**, versus **{prior.ebitda_margin_pct:.1f}%** in FY2024.

## Revenue mix
Toll usage fees remain the dominant revenue stream. Fines are a meaningful but smaller contribution, while tag activation and miscellaneous revenues add ancillary diversification. In FY2025, the company reported growth following variable pricing introduced in January and the first full year of operation of two new gates that opened in November 2024.

## Analyst interpretation
FY2025 growth is unusually strong relative to the previous year, so a forward model should not mechanically extrapolate the full 35% growth rate. Separate one-off expansion/pricing effects from underlying trip growth, test tariff and traffic assumptions, and consider concession duration, related-party arrangements, financing costs and dividend policy.

*EBITDA and free-cash-flow headline values are rounded where source materials provide rounded summaries. The historical series is for educational analysis and is not a substitute for audited financial statements.*
"""
(OUT/"financial_highlights.md").write_text(report, encoding="utf-8")
print(report)
