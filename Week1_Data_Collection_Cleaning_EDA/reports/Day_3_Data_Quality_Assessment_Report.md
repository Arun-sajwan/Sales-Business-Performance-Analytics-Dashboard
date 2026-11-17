# Day 3 – Data Quality Assessment Report

## Project
Sales & Business Performance Analytics Dashboard

## 1. Objective
Assess the original Superstore dataset for duplicate records, row grain, numeric anomalies, date validity, and categorical consistency.

This stage is assessment only. The raw dataset was not modified, cleaned, or exported.

## 2. Dataset overview

| Metric | Result |
|---|---:|
| Rows | 10,194 |
| Columns | 21 |
| Unique Row IDs | 10,194 |
| Unique Order IDs | 5,111 |

## 3. Duplicate and row-grain findings

| Check | Result |
|---|---:|
| Exact duplicate rows | 0 |
| Duplicate Row IDs | 0 |
| Order IDs appearing more than once | 2,518 |
| Maximum rows for one order | 14 |

Every row has a unique Row ID. Multiple rows can share an Order ID because an order may contain multiple product lines. The dataset therefore appears to use an order-line-level grain rather than one row per order.

Repeated Order IDs are not classified as duplicate records.

## 4. Numeric value findings

| Field | Minimum | Maximum | Zero values | Negative values |
|---|---:|---:|---:|---:|
| Quantity | 1 | 14 | 0 | 0 |
| Discount | 0.0 | 0.8 | 4,925 | 0 |
| Sales | 0.444 | 22,638.48 | 0 | 0 |
| Profit | -6,599.978 | 8,399.976 | 65 | 1,901 |

Additional checks:
- Quantity values less than or equal to zero: 0
- Discount values outside the 0–1 range: 0

Negative Profit values may represent legitimate losses or discounted transactions. They should not automatically be treated as invalid data or removed.

## 5. Date validation

| Check | Result |
|---|---:|
| Invalid Order Dates | 0 |
| Invalid Ship Dates | 0 |
| Ship Date earlier than Order Date | 0 |

No date-ordering issue was identified by these checks.

## 6. Categorical consistency

| Field | Unique values | Leading/trailing whitespace |
|---|---:|---:|
| Ship Mode | 4 | 0 |
| Segment | 3 | 0 |
| Country/Region | 2 | 0 |
| Region | 4 | 0 |
| Category | 3 | 0 |
| Sub-Category | 17 | 0 |

No leading or trailing whitespace was found in the inspected categorical fields.

## 7. Key observations

1. No exact duplicate records or duplicate Row IDs were detected.
2. Repeated Order IDs are consistent with multiple product lines per order.
3. Quantity, Discount, and Sales passed the specified basic validity checks.
4. Negative Profit values were observed and should be retained pending business interpretation.
5. Date parsing and chronological checks found no issues.
6. The inspected categorical fields showed no leading or trailing whitespace.

## 8. Conclusion

The checks performed did not identify obvious structural, numeric, date, or label-format errors. This does not guarantee that every field is error-free; additional business-rule checks may be appropriate during later stages.

The raw source file remains unchanged. No cleaning or transformation was performed as part of Day 3.

## 9. Deliverable

- `notebooks/Day_3_Data_Quality_Assessment.ipynb`
- `reports/Day_3_Data_Quality_Assessment_Report.md`
