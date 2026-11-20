# Day 6 Report: Cleaned Dataset Verification and Order-Level Structure

## 1. Objective

Verify the cleaned Superstore dataset produced during Week 1, examine its order-item structure, and build a temporary order-level aggregation for the Week 2 KPI, product, customer, and regional analyses.

## 2. Input and Scope

- **Input:** `data/processed/cleaned_superstore.csv`
- **Notebook:** `Week2_KPI_Product_Customer_Region_Analysis/notebooks/Day_6_Cleaned_Dataset_Verification_and_Order_Level_Structure.ipynb`
- The cleaned dataset was used as the input. The raw source data and previous Week 1 deliverables were not modified.
- The order-level aggregation was created in notebook memory for validation and analysis. It was not exported as a permanent dataset.

## 3. Cleaned Dataset Profile

| Metric | Result |
|---|---:|
| Rows (order-item records) | 10,194 |
| Columns | 21 |
| Unique Order IDs | 5,111 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Duplicate Row IDs | 0 |
| Invalid Order Dates | 0 |
| Invalid Ship Dates | 0 |
| Ship dates before order dates | 0 |

All 21 columns contain non-null values. Order Date and Ship Date are parsed as datetime fields. Sales, Quantity, Discount, and Profit retain numeric data types. Postal Code is stored as text to preserve postal-code formatting, including leading zeros and alphanumeric values.

## 4. Order and Order-Item Structure

The cleaned dataset contains one row per order item, rather than one row per order.

| Metric | Result |
|---|---:|
| Total order-item rows | 10,194 |
| Unique orders | 5,111 |
| Orders containing one item | 2,593 |
| Orders containing multiple items | 2,518 |
| Maximum items in one order | 14 |
| Average items per order | 1.9945 |

The analysis confirms that order counts must be calculated using distinct Order IDs. Counting rows would measure order items, not orders.

## 5. Order-Level Aggregation

A temporary order-level dataset was created by grouping the cleaned records by Order ID.

The aggregation includes order-level dates and customer/order attributes, item counts, distinct product and category counts, and aggregated Sales, Quantity, Discount, and Profit measures.

The resulting dataset contains:

- 5,111 rows, one per unique order.
- 22 columns.
- No duplicate Order IDs.

### Handling inconsistent order attributes

The consistency checks identified the following field-level conflicts:

| Attribute | Orders with conflicting values |
|---|---:|
| Customer ID | 2 |
| City | 2 |
| Postal Code | 2 |

For these attributes, the aggregation does not silently select an arbitrary first value when multiple values exist. It records `MULTIPLE` and sets a corresponding Boolean conflict flag:

- `Customer_ID_Conflict`
- `City_Conflict`
- `Postal_Code_Conflict`

The counts are reported independently for each attribute; they do not establish that the same orders are affected in every field.

## 6. Order-Level Validation and Reconciliation

The aggregation was validated against the source order-item dataset.

| Validation | Result |
|---|---:|
| Unique Order IDs in source | 5,111 |
| Rows in order-level dataset | 5,111 |
| Duplicate Order IDs in order-level dataset | 0 |
| Orders with conflicting Customer IDs | 2 |
| Orders with conflicting Cities | 2 |
| Orders with conflicting Postal Codes | 2 |

### Measure reconciliation

| Measure | Source order-item total | Order-level total |
|---|---:|---:|
| Sales | 2,326,534 | 2,326,534 |
| Profit | 292,296.8 | 292,296.8 |
| Quantity | 38,654 | 38,654 |

The source and aggregated totals reconcile. The notebook's validation assertions passed.

## 7. Limitations and Notes

- The order-level aggregation is temporary and exists in notebook memory; it has not been exported.
- The cleaned order-item dataset remains the authoritative source for product-level and line-item analysis.
- Conflicting customer and location attributes are explicitly flagged rather than silently resolved.
- The cleaned dataset does not contain an `Order Status` column. Therefore, order status was not included in the aggregation or analysis.

## 8. Conclusion

Day 6 successfully verified the cleaned dataset and established the distinction between order-item records and unique orders. The temporary order-level structure contains one record for each of the 5,111 orders, handles inconsistent attributes transparently, and reconciles Sales, Profit, and Quantity totals with the source data.

The cleaned dataset and validated order-level structure provide a sound starting point for the Week 2 KPI, product/category, customer, and regional analyses.

## 9. Execution Summary

- Notebook execution: **Passed**
- Code cells executed: **8**
- Execution errors: **0**
- Order-level validation: **Passed**
- Source-to-aggregation measure reconciliation: **Passed**
