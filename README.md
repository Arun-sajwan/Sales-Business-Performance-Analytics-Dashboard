# Sales & Business Performance Analytics

An end-to-end analytics project covering sales, revenue, profit (where supported), product/category performance, customer segments, regional performance, trends, and an interactive dashboard.

## Weekly workflow
- **Week 1 — Data Collection, Cleaning & EDA:** document the source, inspect data quality, create a data dictionary, clean the data, and perform initial exploratory analysis.
- **Week 2 — KPI, Product, Customer & Region Analysis:** calculate supported KPIs and compare product/category, customer-segment, and regional performance.
- **Week 3 — Trend Analysis & Business Insights:** analyze time-based patterns, investigate changes, document findings, and develop evidence-based recommendations.
- **Week 4 — Dashboard, Final Report & Presentation:** build and validate an interactive Power BI/Tableau dashboard and prepare the final report and presentation.

## Data folders
- `data/raw/` — original, unchanged source files.
- `data/interim/` — intermediate cleaning/transformation files.
- `data/processed/` — final analysis-ready data.

Keep one copy of the original dataset in `data/raw/`; do not duplicate it in each weekly folder.

## Getting started
1. Add the source dataset to `data/raw/`.
2. Record the source, download date, usage conditions, row-level grain, date coverage, and limitations in the Week 1 source notes.
3. Complete the work in weekly order and save each output in its matching folder.
4. Update this README as the project develops.

## Analysis checks
- Confirm what one row represents before counting orders.
- Use distinct valid order IDs for order volume when the data contains multiple order lines.
- Calculate only metrics supported by available fields. Do not estimate profit without reliable cost data.
- Document treatment of discounts, returns, taxes, shipping, missing values, and duplicates.
- Compare equivalent time periods for growth calculations.
- Avoid causal claims from descriptive analysis alone.

## Planned deliverables
Cleaned data, data dictionary, cleaning code, EDA notebook, KPI definitions and tables, product/customer/region analysis, trend visualizations, findings, recommendations, interactive dashboard, final report, and presentation.

## Setup
Install dependencies with:
```bash
python -m pip install -r requirements.txt
```
