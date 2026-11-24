# Day 9 — Source and Processed Dataset Reconciliation Report

## 1. Objective

The objective of Day 9 was to verify that the processed Superstore dataset
preserves the records and business values from the original source dataset.

The reconciliation checks dataset dimensions, numerical totals, order counts,
duplicate records, missing values, Row ID integrity, and row-level field values.

## 2. Datasets Used

| Dataset | File |
|---|---|
| Source | `data/raw/sample_-_superstore.xls` |
| Processed | `data/processed/cleaned_superstore.csv` |

## 3. Dataset Structure

| Metric | Source | Processed |
|---|---:|---:|
| Rows | 10,194 | 10,194 |
| Columns | 21 | 21 |
| Unique orders | 5,111 | 5,111 |
| Unique Row IDs | 10,194 | 10,194 |
| Duplicate rows | 0 | 0 |
| Missing cells | 0 | 0 |

**Result:** Both datasets have matching dimensions and column names/order.

## 4. Numerical Aggregate Reconciliation

The following totals were calculated independently from both datasets.

| Field | Source Total | Processed Total | Absolute Difference | Row-level mismatches above tolerance |
|---|---:|---:|---:|---:|
| Sales | 2,326,534.3543 | 2,326,534.3543 | 0.000000000000 | 0 |
| Profit | 292,296.8146 | 292,296.8146 | 0.000000000000 | 0 |
| Quantity | 38,654.0000 | 38,654.0000 | 0.000000000000 | 0 |
| Discount | 1,583.9900 | 1,583.9900 | 0.000000000000 | 0 |

The numerical aggregate comparisons passed using an absolute tolerance of
`1e-08`.

## 5. Row ID Integrity

| Validation | Result |
|---|---:|
| Source unique Row IDs | 10,194 |
| Processed unique Row IDs | 10,194 |
| Source IDs missing from processed | 0 |
| Extra IDs in processed | 0 |
| Common records aligned for comparison | 10,194 |

All source records have corresponding processed records. No additional processed
Row IDs were found.

## 6. Row-Level Numerical Validation

Sales, Profit, Quantity and Discount were compared record by record after
aligning both datasets using `Row ID`.

The comparison used an absolute tolerance of `1e-8`.

| Field | Result |
|---|---|
| Sales | PASS |
| Profit | PASS |
| Quantity | PASS |
| Discount | PASS |

No row-level numerical differences exceeded the selected tolerance.

### Floating-Point Precision Note

An earlier exact comparison identified:
- Sales: 1,062 exact representation differences
- Profit: 1,442 exact representation differences

The maximum absolute difference for either field was approximately
`4.547474e-13`, far below the `1e-8` validation tolerance.

These differences are consistent with floating-point decimal serialization
and do not indicate meaningful changes to the underlying numerical values.

## 7. All-Column Comparison

All 20 data columns other than the Row ID index were compared after aligning
records by Row ID.

- Numerical fields were compared using the `1e-8` absolute tolerance.
- Non-numerical fields were compared using string representations, with
  missing values handled explicitly.
- No mismatches remained under these comparison rules.

**Result: PASS**

## 8. Final Validation Checklist

| No. | Validation | Result |
|---:|---|---|
| 1 | Dataset dimensions match | PASS |
| 2 | Column names and order match | PASS |
| 3 | Sales total matches within tolerance | PASS |
| 4 | Profit total matches within tolerance | PASS |
| 5 | Quantity total matches within tolerance | PASS |
| 6 | Discount total matches within tolerance | PASS |
| 7 | Unique order counts match | PASS |
| 8 | No source records missing | PASS |
| 9 | No extra processed records | PASS |
| 10 | All Row IDs are unique | PASS |
| 11 | No duplicate rows introduced | PASS |
| 12 | No missing values introduced | PASS |
| 13 | Numerical row-level comparisons pass | PASS |
| 14 | All-column comparisons pass | PASS |

**Validation checks passed: 14 / 14**

## 9. Conclusion

The source and processed Superstore datasets successfully passed all 14
reconciliation checks.

Both datasets contain the same 10,194 records and 21 columns. All Row IDs
are accounted for, aggregate numerical totals match within tolerance, and
row-level numerical and all-column comparisons pass.

The small exact differences observed in Sales and Profit are floating-point
representation differences below the selected tolerance. They are not
evidence of meaningful data alteration.

The reconciliation therefore confirms that the processed dataset preserves
the source dataset's records and compared business values under the
documented validation rules.

## 10. Reproducibility

The executed notebook containing the code, outputs, and validation checklist is:

`Week2_KPI_Product_Customer_Region_Analysis/notebooks/Day_9_Source_and_Processed_Dataset_Reconciliation.ipynb`

Notebook execution completed with six code cells executed and zero errors.
