# Day 4 – Data Standardization Report

## 1. Objective

Standardize date fields, text fields, categorical values, and postal codes in the Superstore dataset using Pandas while preserving the original raw dataset.

## 2. Source and Output

- **Source:** `data/raw/sample_-_superstore.xls`
- **Processed output:** `data/processed/standardized_superstore.csv`
- **Original dataset:** 10,194 rows × 21 columns
- **Processed dataset:** 10,194 rows × 21 columns

All transformations were performed on a separate DataFrame copy. The original raw file was not modified.

## 3. Standardization Performed

### Date fields

- Converted `Order Date` and `Ship Date` consistently using Pandas datetime parsing.
- Confirmed both columns contain valid dates.
- Order Date range: 2023-01-03 to 2026-12-30.
- Ship Date range: 2023-01-07 to 2027-01-05.

### Text fields

- Removed leading and trailing whitespace from applicable text columns.
- Preserved existing capitalization and source labels.
- Kept identifiers and product/customer names intact.

### Categorical fields

Inspected the following categorical columns:

- Ship Mode
- Segment
- Country/Region
- Region
- Category
- Sub-Category

The category labels were already consistent. No category renaming or unnecessary value changes were required.

### Postal Code

- Identified mixed integer and string values in the original column.
- Converted Postal Code to Pandas string dtype.
- Preserved numeric and alphanumeric postal codes as text.
- Verified that all 10,194 postal-code values were preserved.
- Avoided numeric conversion that could remove leading zeros.

## 4. Validation Results

| Validation | Result |
|---|---:|
| Original row count | 10,194 |
| Exported row count | 10,194 |
| Original and exported columns | 21 each |
| Missing values in processed dataset | 0 |
| Duplicate rows | 0 |
| Missing postal codes after export | 0 |
| Postal-code values preserved | Yes |
| Invalid date ordering | 0 |
| Date columns parsed successfully | Yes |
| Expected category values retained | Yes |

## 5. Output

The standardized dataset was exported to:

`data/processed/standardized_superstore.csv`

The exported CSV is approximately 2.36 MB.

## 6. Conclusion

Day 4 standardization was completed successfully. Date fields were parsed consistently, text fields were standardized without changing source meaning, existing category labels were retained, and postal codes were converted to string format without losing values.

The processed dataset passed the validation checks. The original raw dataset remains unchanged.
