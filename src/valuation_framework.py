from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/"outputs"
df = pd.read_csv(ROOT/"data"/"historical_financials.csv").sort_values("fiscal_year")
latest = df.iloc[-1]
# A simple scenario grid for implied enterprise value, using an analyst-defined EBITDA multiple.
# This is deliberately not a share-price target: market cap, debt, cash and date-consistent multiples
# must be sourced separately before a listed-company valuation can be completed.
multiples = [12, 14, 16, 18, 20]
rows = []
for multiple in multiples:
    rows.append({
        "illustrative_ev_ebitda_multiple_x": multiple,
        "implied_enterprise_value_aed_m": latest.ebitda_aed_m * multiple,
        "method": "FY2025 EBITDA multiplied by illustrative multiple",
        "status": "scenario only; not market-observed multiple"
    })
pd.DataFrame(rows).to_csv(OUT/"illustrative_ev_sensitivity.csv", index=False)

peer_template = pd.DataFrame([
    {"company":"Salik Company P.J.S.C.","ticker":"SALIK (ADX)","valuation_date":"","market_cap_aed_m":np.nan,"net_debt_aed_m":np.nan,"ev_aed_m":np.nan,"ltm_ebitda_aed_m":latest.ebitda_aed_m,"ev_ebitda_x":np.nan,"source_url":"","comparability_notes":"Subject company; source current market capitalization, cash/debt and market date before calculating multiples."},
    {"company":"Peer 1 — select and verify","ticker":"","valuation_date":"","market_cap_aed_m":np.nan,"net_debt_aed_m":np.nan,"ev_aed_m":np.nan,"ltm_ebitda_aed_m":np.nan,"ev_ebitda_x":np.nan,"source_url":"","comparability_notes":"Choose a listed toll-road or infrastructure operator and explain differences in concession and leverage."},
    {"company":"Peer 2 — select and verify","ticker":"","valuation_date":"","market_cap_aed_m":np.nan,"net_debt_aed_m":np.nan,"ev_aed_m":np.nan,"ltm_ebitda_aed_m":np.nan,"ev_ebitda_x":np.nan,"source_url":"","comparability_notes":"Keep valuation date, currency and EBITDA definition consistent."},
    {"company":"Peer 3 — select and verify","ticker":"","valuation_date":"","market_cap_aed_m":np.nan,"net_debt_aed_m":np.nan,"ev_aed_m":np.nan,"ltm_ebitda_aed_m":np.nan,"ev_ebitda_x":np.nan,"source_url":"","comparability_notes":"Exclude or flag businesses with materially different concession structures or business mixes."},
])
peer_template.to_csv(ROOT/"data"/"peer_benchmark_template.csv", index=False)
print(pd.DataFrame(rows).to_string(index=False))
