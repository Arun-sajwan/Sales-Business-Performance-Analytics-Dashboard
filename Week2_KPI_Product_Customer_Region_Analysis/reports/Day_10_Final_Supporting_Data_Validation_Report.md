# Day 10 — Final Supporting Data Validation Report

## 1. Objective

Perform final supporting data-quality checks on the cleaned Superstore dataset. The work covers categorical values, product hierarchy relationships, dates, identifiers, business rules, order-level consistency, source anomaly verification, and return-data availability.

The purpose is to establish whether the processed dataset preserves the source data and satisfies the selected structural and business validation rules.

## 2. Datasets Used

| Dataset | Path | Role |
|---|---|---|
| Original source | `data/raw/sample_-_superstore.xls` | Source-level verification |
| Cleaned dataset | `data/processed/cleaned_superstore.csv` | Supporting validation target |

The cleaned dataset contains **10,194 rows and 21 columns**. No missing cells were observed.

The original source and cleaned dataset were not modified during validation.

## 3. Categorical Field Validation

Six categorical fields were checked for missing values and whitespace-only entries.

| Field | Unique values | Missing | Whitespace-only |
|---|---:|---:|---:|
| Ship Mode | 4 | 0 | 0 |
| Segment | 3 | 0 | 0 |
| Country/Region | 2 | 0 | 0 |
| Region | 4 | 0 | 0 |
| Category | 3 | 0 | 0 |
| Sub-Category | 17 | 0 | 0 |

All six categorical fields passed the missing-value and whitespace checks.

### Category and Sub-Category Relationship

The expected product hierarchy was checked against the observed values.

| Category | Expected sub-categories | Observed sub-categories | Result |
|---|---:|---:|---|
| Furniture | 4 | 4 | PASS |
| Office Supplies | 9 | 9 | PASS |
| Technology | 4 | 4 | PASS |
| **Total** | **17** | **17** | **PASS** |

- Missing expected sub-categories: 0
- Unexpected sub-categories: 0
- Invalid Category/Sub-Category rows: 0
- Unexpected categories: 0

The observed product hierarchy matches the expected mapping.

## 4. Date Integrity Validation

Both date fields were parsed and checked for invalid values and chronological violations.

| Check | Result |
|---|---:|
| Invalid Order Dates | 0 |
| Invalid Ship Dates | 0 |
| Ship Date before Order Date | 0 |
| Same-day shipping records | 523 |
| Minimum shipping duration | 0 days |
| Maximum shipping duration | 11 days |

Date ranges:

- Order Date: January 3, 2023 – December 30, 2026
- Ship Date: January 7, 2023 – January 5, 2027

Shipping duration distribution:

| Duration | Records |
|---:|---:|
| 0 days | 523 |
| 1 day | 369 |
| 2 days | 1,361 |
| 3 days | 1,025 |
| 4 days | 2,838 |
| 5 days | 2,243 |
| 6 days | 1,204 |
| 7 days | 629 |
| 11 days | 2 |

No invalid dates or negative shipping durations were identified. The two 11-day shipments were retained; duration alone does not establish that they are invalid.

**Date integrity result: PASS.**

## 5. Identifier Integrity

Four identifier fields were examined.

| Identifier | Unique values | Duplicate rows | Missing values |
|---|---:|---:|---:|
| Row ID | 10,194 | 0 | 0 |
| Order ID | 5,111 | 5,083 | 0 |
| Customer ID | 804 | 9,390 | 0 |
| Product ID | 1,862 | 8,332 | 0 |

Repeated Order IDs, Customer IDs, and Product IDs are expected in an order-item-level dataset. They do not automatically indicate duplicate records.

Additional checks:

- Blank identifier values: 0
- Row ID minimum: 1
- Row ID maximum: 10,194
- Row IDs form a continuous sequence.
- Rows per order: minimum 1, maximum 14.
- Average rows per order: approximately 1.99.

**Identifier integrity result: PASS.**

## 6. Business Rule Validation

Eight business rules were tested.

| Business rule | Result |
|---|---|
| Sales greater than zero | PASS |
| Quantity is positive | PASS |
| Quantity contains whole numbers | PASS |
| Discount between 0 and 1 | PASS |
| Profit contains valid numeric values | PASS |
| Postal Code has no blank strings | PASS |
| Ship Mode belongs to expected categories | PASS |
| Segment belongs to expected categories | PASS |

Numerical boundaries:

| Field | Minimum | Maximum |
|---|---:|---:|
| Sales | 0.444 | 22,638.48 |
| Quantity | 1 | 14 |
| Discount | 0.0 | 0.8 |
| Profit | -6,599.978 | 8,399.976 |

Business-value observations:

- Negative-profit rows: 1,901
- Zero-profit rows: 65
- Positive-profit rows: 8,228
- Zero-discount rows: 4,925
- Maximum discount: 80%

Negative profit is retained because loss-making transactions are legitimate business outcomes. It is not treated as an automatic data-quality error.

**Business rule result: 8/8 PASS.**

## 7. Order-Level Consistency and Source Anomalies

Order-level consistency was checked across customer, date, shipping, and geographic fields.

| Field | Inconsistent orders | Result |
|---|---:|---|
| Customer ID | 2 | Review |
| Customer Name | 0 | PASS |
| Order Date | 0 | PASS |
| Ship Date | 0 | PASS |
| Ship Mode | 0 | PASS |
| Segment | 0 | PASS |
| Country/Region | 0 | PASS |
| City | 2 | Review |
| State/Province | 0 | PASS |
| Postal Code | 2 | Review |
| Region | 0 | PASS |

This produced six field/order inconsistencies across the three affected fields.

### 7.1 Customer ID anomalies

Orders `CA-2025-121465` and `CA-2026-130494` contain multiple Customer IDs:

- HO-15234
- HO-15233
- HO-15232
- HO-15231

The rows show the same customer name, Harry Olson, and the same geographic information.

### 7.2 City and Postal Code anomalies

Orders `CA-2023-131807` and `CA-2026-131807` contain two city and postal-code combinations:

| City | State/Province | Postal Code |
|---|---|---|
| Calgary | Alberta | T1Y |
| Edmonton | Alberta | T5A |

### 7.3 Original Source Comparison

All four affected orders were inspected in the original Excel source and the cleaned CSV.

The relevant values, including Row ID, Order ID, Customer ID, customer name, city, province, postal code, country, product ID, and product name, matched between the two datasets.

**Conclusion:** These inconsistencies are already present in the original source. The cleaned dataset preserves them without introducing changes.

**Decision:** Retain the original values and document these as inherited source-level anomalies. Do not silently assign new customer IDs or replace city and postal-code values.

## 8. Return Data Availability

No return-related fields were found in the 21-column cleaned dataset.

Therefore:

- Return validation: Not applicable.
- Returned-order identification: Not supported by the available fields.
- Return analysis: Cannot be independently performed using this dataset.

This is a dataset limitation, not a failed validation.

## 9. Final Validation Checklist

| Validation area | Result |
|---|---|
| Categorical fields | PASS |
| Category/Sub-Category mapping | PASS |
| Date integrity | PASS |
| Identifier integrity | PASS |
| Business rules | 8/8 PASS |
| Order-level consistency | Source-level anomalies confirmed |
| Source anomaly verification | PASS |
| Return data availability | Not applicable |

**Primary validation result: 6/6 validation groups passed** (categorical fields, category mapping, date integrity, identifier integrity, business rules, and source anomaly verification).

The order-level inconsistencies were confirmed against the original source and retained unchanged. Return analysis remains outside the scope supported by the available dataset.

## 10. Conclusion

The Day 10 supporting data-validation review confirms that the cleaned dataset has consistent categorical values, a valid product hierarchy, parseable dates, correct shipping chronology, valid identifiers, and values that satisfy the selected business rules.

The review identified six field/order inconsistencies across Customer ID, City, and Postal Code. Comparison with the original source confirmed that these are inherited source-level anomalies rather than processing changes.

No return-related fields are available, so return validation is not applicable.

The cleaned dataset remains unchanged. The validation notebook provides reproducible checks and the report records the findings and limitations.

## 11. Reproducibility

Run the notebook from the repository root:

`Week2_KPI_Product_Customer_Region_Analysis/notebooks/Day_10_Final_Supporting_Data_Validation.ipynb`

Required input files:

- `data/raw/sample_-_superstore.xls`
- `data/processed/cleaned_superstore.csv`

Required Python packages:

- pandas
- numpy
- openpyxl or xlrd, as required by the installed Excel-reading engine
- nbformat for notebook handling

The notebook reads the source and processed datasets and performs the supporting checks without modifying either input file.
