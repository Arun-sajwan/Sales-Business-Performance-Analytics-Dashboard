# Sales & Business Performance Analytics Dashboard

An end-to-end analytics project covering sales, revenue, profit (where supported), product/category performance, customer segments, regional performance, trends, and an interactive dashboard.

In this project, we will analyze sales data and present important business insights through an interactive dashboard.

## Business problem

Businesses need to understand how effectively they are performing. This project investigates potential problems such as decreasing sales, low-performing products or categories, declining profit, regional performance differences, changing customer purchasing patterns, and discounts that may reduce profitability.

For example, when sales decline, the goal is to identify which products, categories, or regions contributed to the decline and support appropriate business action.

## Analysis objectives

1. Analyze total sales and total profit.
2. Identify top-performing and low-performing products.
3. Compare sales and profit across regions.
4. Analyze monthly and yearly sales trends.
5. Understand customer purchasing patterns.
6. Examine the effect of discounts on sales and profit.
7. Present useful insights that support informed, data-driven decisions.

## Key performance indicators

| KPI | Purpose |
|---|---|
| Total Sales | Measures total revenue generated from sales |
| Total Profit | Measures profit earned by the business |
| Total Orders | Shows the number of orders received |
| Profit Margin | Shows the percentage of sales retained as profit |
| Average Order Value (AOV) | Shows the average value of each order |
| Sales Growth | Tracks how sales change over time |

KPIs will be calculated only where the source dataset contains the required fields. Order counts and AOV should use valid, distinct order IDs when the dataset contains multiple order lines.

## Expected outcome

The project will produce an interactive Sales and Business Analytics Dashboard that helps users:

- Monitor overall sales and profit performance.
- Identify high-performing and low-performing products.
- Compare performance across regions and time periods.
- Understand important trends and patterns.
- Make informed, data-driven business decisions.

## Weekly workflow

- **Week 1 — Data Collection, Cleaning & EDA:** document the source, inspect data quality, create a data dictionary, clean the data, and perform initial exploratory analysis.
- **Week 2 — KPI, Product, Customer & Region Analysis:** calculate supported KPIs and compare product/category, customer-segment, and regional performance.
- **Week 3 — Trend Analysis & Business Insights:** analyze time-based patterns, investigate changes, document findings, and develop evidence-based recommendations.
- **Week 4 — Dashboard, Final Report & Presentation:** build and validate an interactive Power BI/Tableau dashboard and prepare the final report and presentation.

## Data folders

- `data/raw/` — original, unchanged source files.
- `data/interim/` — intermediate cleaning/transformation files.
- `data/processed/` — final analysis-ready data.

Keep one copy of the original dataset in `data/raw/`;

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
