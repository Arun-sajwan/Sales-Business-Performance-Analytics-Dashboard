# Week 2 Integration Notes

## Purpose

These notes define how the Week 2 KPI, product, customer, and regional outputs fit together and how they should be reused in later dashboard, trend, and reporting work.

## Week 1 report references

The following Week 1 reports provide the baseline data-quality, EDA, and KPI context used by this Week 2 integration:

- [EDA Analysis Results](Week1_Data_Collection_Cleaning_EDA/reports/EDA_Analysis_Results.xlsx) - contains the recorded exploratory-analysis outputs that support the initial sales, profit, product, category, customer, and regional observations.
- [KPI Summary](Week1_Data_Collection_Cleaning_EDA/reports/KPI_Summary.xlsx) - provides the Week 1 KPI baseline and reference results for comparison with the detailed Week 2 analysis.
- [Final KPI Report](Week1_Data_Collection_Cleaning_EDA/reports/Final%20KPI%20Report.docx) - presents the final KPI conclusions and should be reviewed alongside the detailed Week 2 calculations.
- Supporting analysis files: Multiple Week 1 & week 2 analysis workbooks, spreadsheets, notebooks, and reports were used to establish the project baseline. Review the complete set under `Week1_Data_Collection_Cleaning_EDA/` And `Week2_KPI_Product_Customer_Region_Analysis/`, rather than relying on any one file alone.

Before using these reports as sources of truth, confirm their date coverage and calculation grain against `data/processed/cleaned_superstore.csv` and `data/processed/standardized_superstore.csv`.

## Integrated source

- Analysis source: `data/processed/cleaned_superstore.csv`
- Standardized source: `data/processed/standardized_superstore.csv`
- Week 1 EDA results: `Week1_Data_Collection_Cleaning_EDA/reports/EDA_Analysis_Results.xlsx`
- Week 1 KPI summary: `Week1_Data_Collection_Cleaning_EDA/reports/KPI_Summary.xlsx`
- Week 1 final KPI report: `Week1_Data_Collection_Cleaning_EDA/reports/Final KPI Report.docx`
- Week 2 workbook: `Week2_KPI_Product_Customer_Region_Analysis/kpi_tables/Dashbord_data_.xlsx`
- Each source row represents one order line; an `Order ID` can contain multiple product lines.

The processed datasets contain 10,194 transaction rows, 5,111 distinct orders, and 804 distinct customers. The overall totals are $2,326,534.35 in sales, $292,296.81 in profit, a 12.56% profit margin, and $455.20 average order value.

## KPI integration

Use the following grain and formulas consistently:

| KPI | Integration formula | Required grain |
|---|---|---|
| Total Sales | Sum of `Sales` | Any selected dimension or period |
| Total Profit | Sum of `Profit` | Any selected dimension or period |
| Order Volume | Distinct count of `Order ID` | Period, region, customer, or segment |
| Quantity Sold | Sum of `Quantity` | Product or category analysis |
| Average Order Value | Total Sales / distinct `Order ID` | Period or customer view |
| Profit Margin | Total Profit / Total Sales | Aggregated period or dimension |
| Sales Growth | (Current period Sales - prior period Sales) / prior period Sales | Matching periods |

Do not average pre-calculated profit margins or average order values. Calculate the ratio from the underlying aggregated totals. Do not sum category, regional, or sub-category order counts to obtain a business-wide order count.

## Product and category integration

Product and category analysis should use the same total-sales and total-profit definitions used by the KPI summary. Negative profit values are valid business results and must remain in the dataset.

Week 1 and Week 2 findings are consistent on the main category and sub-category issues:

- Technology leads sales and profit.
- Office Supplies has strong sales and a strong profit margin.
- Furniture has a low overall profit margin.
- Tables are a major loss-making sub-category.
- Copiers, Accessories, and Phones are important profit contributors.

Product rankings should be based on aggregated sales or profit within the selected period, not on row count. Loss-making products should remain visible and should not be hidden by filtering negative profit.

## Customer and regional integration

Customer metrics should use distinct `Order ID` values for order counts and total sales/profit for all lines associated with each customer.

The regional summary should reconcile to the full processed-data totals:

| Region | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| West | $739,813.61 | $110,798.82 | 14.98% |
| East | $691,828.17 | $99,329.60 | 14.36% |
| Central | $503,170.67 | $39,842.45 | 7.92% |
| South | $391,721.91 | $46,739.94 | 11.93% |

Before reporting a regional or customer ranking, confirm that the analysis uses the same date filter and the same customer/region membership.

## Workbook reconciliation

The `Dashbord_data_.xlsx` workbook contains summarized analysis sheets. It should be used as a presentation-ready summary, while final KPI calculations should derive from the transaction-level processed CSV.

The workbook's annual table stops at 30 December for 2023, 2024, and 2025. The processed full-date data contains rows dated 31 December in those years. This causes the following differences:

| Year | Rows omitted after 30 Dec | Sales omitted | Profit omitted | Orders omitted |
|---|---:|---:|---:|---:|
| 2023 | 14 | $5,253.27 | $1,444.51 | 7 |
| 2024 | 11 | $1,381.34 | $438.49 | 5 |
| 2025 | 7 | $731.77 | $68.24 | 5 |

The annual workbook totals reconcile with the processed data when the 31 December rows are excluded. Category and regional sheets use the full-date totals, so they should not be compared directly with annual rows that stop one day earlier unless a matching date filter is applied.

The workbook currently compares 2026 with 2025 and reports sales growth of 21.59%, profit growth of 16.14%, order-growth of 29.06%, and a 0.60 percentage-point decline in profit margin. These results should be labeled as comparing the available ranges until 30 December rather than as a complete 2026 or 2025 calendar-year comparison.

## Future-date check

The source contains 524 order lines dated after 26 November 2026. These rows represent 260 orders, $100,843.40 in sales, and $9,745.35 in profit. Because they extend beyond the current project date, Week 3 and Week 4 views should explicitly confirm whether they are valid future/planned records or should be excluded from current-performance reporting.

## Dashboard integration rules

The following filters and measures should be connected across all dashboard views:

- Date range
- Region
- Customer segment
- Category
- Sub-category
- Product
- Customer
- Discount band

All visuals should respond to the same slicers and should use transaction-level measures instead of sums of pre-calculated workbook values. Sales, profit, quantity, order volume, AOV, and profit margin should be clearly labeled as:

- Current selection
- Comparison period
- Variance
- Variance percentage where the denominator is valid

## Week 3

Week 3 should use the Week 2 KPI definitions and aggregated views to investigate:

- Monthly and yearly trends
- Drivers of sales and profit growth
- Category and sub-category changes
- Regional performance gaps
- Customer concentration
- Discount effects
- Seasonal or future-date anomalies

Any finding from Week 3 should cite the relevant dimension, period, sales/profit totals, and date filter so that it can be traced back to the source data.
