# Day 7 — Order ID, Quantity, Discount and Returns Analysis

## 1. Project information

**Project:** Sales Business Performance Analytics Dashboard  
**Week:** 2  
**Analysis day:** 7  
**Focus:** Order IDs, quantities, discounts and returned orders

## 2. Objective

The objective of this analysis is to understand order structure, product quantities, discount patterns and returned orders in the Superstore dataset.

The analysis uses the cleaned Orders dataset and the Returns sheet from the original Excel workbook. Original raw files remain unchanged.

## 3. Data sources

| Source | Purpose | Records |
|---|---|---:|
| `data/processed/cleaned_superstore.csv` | Order, quantity, discount, sales and profit analysis | 10,194 |
| `data/raw/sample_-_superstore.xls` — Returns sheet | Returned-order identification | 296 |

The Orders dataset is at order-item level. Each row represents a product line, while the Returns sheet identifies returned orders using Order ID.

## 4. Order ID analysis

| Metric | Result |
|---|---:|
| Total order-item rows | 10,194 |
| Unique orders | 5,111 |
| Single-item orders | 2,593 |
| Multi-item orders | 2,518 |
| Maximum items in one order | 14 |
| Average items per order | 1.99 |
| Duplicate complete rows | 0 |
| Duplicate Row IDs | 0 |

### Findings

- The dataset contains 5,111 unique orders represented by 10,194 order-item records.
- 2,593 orders contain one item.
- 2,518 orders contain more than one item.
- One order contains a maximum of 14 order items.
- Order counts must use distinct Order IDs rather than counting order-item rows.

## 5. Quantity analysis

| Metric | Result |
|---|---:|
| Total quantity | 38,654 |
| Average quantity per order item | 3.79 |
| Median quantity | 3 |
| Minimum quantity | 1 |
| Maximum quantity | 14 |
| Zero-quantity records | 0 |
| Negative-quantity records | 0 |

### Quantity distribution

| Quantity | Order-item records |
|---:|---:|
| 1 | 933 |
| 2 | 2,440 |
| 3 | 2,435 |
| 4 | 1,212 |
| 5 | 1,269 |
| 6 | 585 |
| 7 | 617 |
| 8 | 269 |
| 9 | 259 |
| 10 | 61 |
| 11 | 34 |
| 12 | 23 |
| 13 | 27 |
| 14 | 30 |

### Findings

- Quantities range from 1 to 14 units per order item.
- Quantities of 2 and 3 are the most frequent.
- No zero or negative quantities were identified.
- The total quantity across all order items is 38,654 units.

## 6. Discount analysis

| Metric | Result |
|---|---:|
| Total order-item records | 10,194 |
| Items with no discount | 4,925 |
| Discounted order items | 5,269 |
| Discounted order-item percentage | 51.69% |
| Average discount | 15.54% |
| Minimum discount | 0% |
| Maximum discount | 80% |

### Sales and profit by discount

| Discount | Order items | Sales | Profit |
|---:|---:|---:|---:|
| 0% | 4,925 | 1,105,323.79 | 326,718.59 |
| 10% | 96 | 54,952.50 | 9,099.97 |
| 15% | 52 | 27,558.52 | 1,418.99 |
| 20% | 3,706 | 773,939.40 | 91,079.95 |
| 30% | 230 | 104,474.07 | -10,513.45 |
| 32% | 27 | 14,493.46 | -2,391.14 |
| 40% | 207 | 116,497.76 | -23,086.37 |
| 45% | 11 | 5,484.97 | -2,493.11 |
| 50% | 66 | 58,918.54 | -20,506.43 |
| 60% | 149 | 7,105.94 | -6,164.35 |
| 70% | 424 | 40,805.27 | -40,300.57 |
| 80% | 301 | 16,980.15 | -30,565.27 |

### Findings

- Approximately 51.69% of order items received a discount.
- The most common discount level is 20%, with 3,706 order items.
- Discount levels of 30% and above show negative aggregate profit in this dataset.
- Order items without discounts have the highest aggregate profit.

**Interpretation limitation:** These results show an association between discount levels and profitability. They do not establish that discounts alone caused the losses. Product mix, category, cost and other factors may also influence profit.

## 7. Returns analysis

The Returns sheet was matched against unique Order IDs in the cleaned Orders dataset.

| Metric | Result |
|---|---:|
| Total unique orders | 5,111 |
| Returns records | 296 |
| Unique returned Order IDs | 296 |
| Matched returned Order IDs | 296 |
| Unmatched returned Order IDs | 0 |
| Duplicate return Order IDs | 0 |
| Missing return Order IDs | 0 |
| Returned status | Yes (296 records) |
| Orders without a return record | 4,815 |
| Return rate | 5.79% |

### Return rate calculation

Return rate is calculated using unique orders:

`Return Rate = (Returned Orders / Total Unique Orders) × 100`

`Return Rate = (296 / 5,111) × 100 = 5.79%`

### Findings

- All 296 returned Order IDs match orders in the cleaned dataset.
- No duplicate or missing Return Order IDs were found.
- The calculated return rate is approximately 5.79%.
- The return rate uses unique orders, not order-item records.

## 8. Consolidated KPI summary

| KPI | Result |
|---|---:|
| Total unique orders | 5,111 |
| Total order items | 10,194 |
| Total units sold | 38,654 |
| Single-item orders | 2,593 |
| Multi-item orders | 2,518 |
| Discounted order items | 5,269 |
| Discounted order-item percentage | 51.69% |
| Returned orders | 296 |
| Orders without a return record | 4,815 |
| Return rate | 5.79% |

## 9. Data validation

The following checks were performed:

- Expected order-item row count: 10,194.
- Expected unique order count: 5,111.
- No duplicate Row IDs.
- No duplicate complete order-item rows.
- All quantities are positive.
- No missing Order IDs.
- Returns sheet contains 296 records.
- Return Order IDs are unique.
- All return IDs match the Orders dataset.
- All Returned status values are `Yes`.

All 10 notebook validation checks passed.

## 10. Business observations

1. Order-item records and unique orders represent different levels of measurement and should not be mixed in KPI calculations.
2. Multi-item orders account for a substantial share of total orders.
3. Quantity values are positive, with quantities of 2 and 3 occurring most frequently.
4. More than half of order items receive a discount.
5. Higher discount levels show negative aggregate profit in this dataset and deserve further investigation.
6. The validated return rate is 5.79%.

## 11. Limitations and methodology notes

- Order counts use distinct Order IDs.
- Quantity and discount calculations use order-item records.
- Return counts use unique Order IDs from the Returns sheet.
- An order without a Returns sheet record is treated as having no recorded return in this dataset; this does not independently verify its physical delivery or final customer outcome.
- Discount-profit relationships are descriptive and do not demonstrate causation.
- Raw source files were not modified.
- No additional cleaned dataset was exported during this analysis.

## 12. Deliverables

**Notebook:**  
`Week2_KPI_Product_Customer_Region_Analysis/notebooks/Day_7_Order_Quantity_Discount_and_Returns_Analysis.ipynb`

**Report:**  
`Week2_KPI_Product_Customer_Region_Analysis/reports/Day_7_Order_Quantity_Discount_and_Returns_Analysis_Report.md`

The notebook contains reproducible analysis, summary tables, charts and validation checks.

---

**Day 7 analysis report**
