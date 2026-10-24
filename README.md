# Salik — Financial Analysis & Valuation Benchmarking

A reproducible financial-analysis portfolio project using three years of reported headline data (FY2023–FY2025), revenue composition, calculated ratios, visualizations, and a transparent valuation-sensitivity framework.

## What's included
- Three-year historical financial dataset.
- Revenue breakdown by toll usage, tag activation, fines, toll gate construction and miscellaneous revenue.
- Growth, margin and cash-flow ratio analysis.
- Python-generated charts and a financial highlights report.
- Illustrative EV/EBITDA sensitivity and a peer-comparison template.
- Written investment thesis, catalysts and risks.

## Quick start
```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/analyze.py
python src/valuation_framework.py
```

## Repository map
```text
data/
  historical_financials.csv
  revenue_breakdown.csv
  peer_benchmark_template.csv
src/
  analyze.py
  valuation_framework.py
outputs/
  ratio_analysis.csv
  financial_highlights.md
  illustrative_ev_sensitivity.csv
  figures/
reports/
  investment_thesis.md
```

## FY2025 findings
Salik reported revenue of AED 3.097bn, EBITDA of AED 2.144bn, net profit of AED 1.553bn, and free cash flow of AED 2.080bn. Revenue grew 35.1% versus FY2024. Management cited variable pricing introduced in January 2025 and the first full year of two new toll gates as major drivers.

## Sources
- [Salik FY2025 Annual Report](https://ar2025.salik.ae/en)
- [FY2025 statement of profit or loss](https://ar2025.salik.ae/en/financial-statements/statement-profit-loss-comprehensive-income)
- [FY2025 notes and revenue breakdown](https://ar2025.salik.ae/en/financial-statements/notes-financial-statements)
- [Salik FY2024 Annual Report](https://ar2024.salik.ae/en)
- [FY2024 statement of profit or loss](https://ar2024.salik.ae/en/financial-statements/statement-profit-loss-comprehensive-income)
- [FY2024 CFO review](https://ar2024.salik.ae/en/strategic-review/cfo-review)

## Valuation limitations
The EV/EBITDA sensitivity uses illustrative multiples and is not a completed comparable-company valuation. The peer template must be populated with real, sourced data from a consistent date. Do not present the scenario output as a market-implied value or share-price target. For a formal valuation, consider the concession term, debt, cash, finance costs, dividends and potential terminal-value limitations.


