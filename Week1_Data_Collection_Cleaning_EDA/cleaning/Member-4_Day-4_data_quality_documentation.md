# Data Quality Documentation

| Document Detail | Information |
|---|---|
| **Project** | Sales & Business Performance Analytics Dashboard |
| **Prepared by** | Member 4 |
| **Week** | 1 — Data Collection, Cleaning & EDA |
| **Review date** | 18 November 2026 |
| **Status** | Draft |

---

## 1. Purpose

This document records the data-quality issues identified in the sales dataset, the actions taken or recommended, and the assumptions that may affect later analysis and dashboard development.

## 2. Dataset Details

| Item | Details |
|---|---|
| Dataset name | Superstore sales sample |
| Source | [Tableau public Superstore sample data](https://public.tableau.com/app/learn/sample-data) |
| Original file | `sample_-_superstore.xls` |
| Worksheet reviewed | `Orders` |
| Number of rows | 10,194 |
| Number of columns | 21 |
| Cleaned dataset | [cleaned_superstore.csv](https://github.com/Arun-sajwan/Sales-Business-Performance-Analytics-Dashboard/tree/main/data/processed/) |
| Reviewed with | Member 1 — Data Collection & Data Cleaning |

## 3. Data Quality Review

The source workbook was inspected on **18 November 2026**. It contains the `Orders`, `People`, and `Returns` worksheets. This review covers the 10,194-row `Orders` worksheet.

| Area Checked | Result | Action Taken | Status |
|---|---|---|---|
| Missing values | No blank cells were found in any of the 21 columns. | No treatment required. | ✅ Complete |
| Duplicate records | No fully duplicated rows were found. `Order ID` is repeated across 10,194 rows, but it represents multi-line orders. | Retain all rows. | ✅ Complete |
| Order IDs | 5,111 distinct order IDs were found. | Count orders using distinct `Order ID` values. | ✅ Complete |
| Date formatting | Both date columns contain valid datetime values. The order-date range is 3 January 2023 to 30 December 2026. | No conversion required. | ✅ Complete |
| Shipping dates | No ship date was earlier than its corresponding order date. | No records removed. | ✅ Complete |
| Category consistency | No leading or trailing whitespace or spelling variations were found in category fields. | No standardization required. | ✅ Complete |
| Invalid or unusual values | 1,901 rows contain negative profit. Sales are positive, quantities are at least 1, and discounts are from 0% to 80%. | Retain negative profit values as observed business losses. | ✅ Complete |
| Data types | Sales, quantity, discount, and profit are numeric; order and ship dates are datetime values. | No conversion required. | ✅ Complete |

## 4. Detailed Issue Log

### Issue 1 — Negative Profit Values

| Field | Description |
|---|---|
| **Affected column** | `Profit` |
| **Finding** | 1,901 of 10,194 rows contain negative profit. |
| **Action** | Retain all values without alteration. |
| **Reason** | Negative profit is a plausible business outcome, and no evidence was found that these values are invalid. |
| **Validation** | Every profit value was checked, and sales and quantity remain valid in the affected rows. |


### Issue 2 — Repeated Order IDs

| Field | Description |
|---|---|
| **Affected column** | `Order ID` |
| **Finding** | 5,111 distinct order IDs occur across 10,194 rows. Therefore, 5,083 additional rows repeat an existing order ID. |
| **Action** | Retain all rows and do not deduplicate by `Order ID`. |
| **Reason** | Each row represents a distinct product line item. `Row ID` is unique, and repeated order IDs indicate valid multi-line orders. |
| **Validation** | All 10,194 `Row ID` values are unique, and no fully duplicated records exist. |


## 5. Cleaning Decisions and Assumptions

- Retain all 10,194 source rows.
- Treat negative profit values as observed business losses.
- Calculate order volume using distinct `Order ID` values rather than row count.
- Retain existing category and sub-category labels.
- Retain existing date values because they are valid and consistently stored as datetime values.
- Do not remove repeated order IDs because they represent legitimate order line items.
- No records or columns were excluded during this source-workbook inspection.

## 6. Source Validation

| Validation Check | Result |
|---|---|
| Workbook opens successfully | ✅ Confirmed |
| `Orders` worksheet is present | ✅ Confirmed |
| 10,194 source rows are present | ✅ Confirmed |
| 21 expected columns are present | ✅ Confirmed |
| Date columns use valid datetime types | ✅ Confirmed |
| Missing values checked | ✅ No missing values found |
| Fully duplicated rows checked | ✅ No duplicated rows found |
| Sales and quantity values checked | ✅ No nonpositive values found |
| Discount values checked | ✅ Values range from 0% to 80% |

### Reference Totals

| Metric | Source Total |
|---|---:|
| Sales | 2,326,534.3543 |
| Profit | 292,296.8146 |

## 7. Files and Repository Locations

| File | Repository Location | Status |
|---|---|---|
| Original dataset | `data/raw/sample_-_superstore.xls` | ✅ Complete |
| Cleaning script | `Week1_Data_Collection_Cleaning_EDA/cleaning/clean_superstore_data.py` or approved project location | ✅ Complete |
| Cleaned dataset | `data/processed/cleaned_superstore.csv` | ✅ Complete |
| Data-quality documentation | `Week1_Data_Collection_Cleaning_EDA/cleaning/Member-4_Day-4_data_quality_documentation.md` | ✅ Draft |


## 8. Conclusion

The source workbook passed the initial data-quality review. No missing values or fully duplicated rows were found, and no cleaning is required for the validated fields.

Negative profit values and repeated order IDs are expected business patterns; they should be retained and handled explicitly in later KPI calculations.
