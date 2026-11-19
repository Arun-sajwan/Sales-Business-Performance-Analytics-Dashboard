# Day 5 – Data Cleaning and Final Dataset Export Report

## 1. Objective

Develop a reusable Python cleaning script, apply the established data standardization rules to the original Superstore dataset, export the cleaned dataset, and validate the exported file.

## 2. Source and Output

- **Source:** `data/raw/sample_-_superstore.xls`
- **Cleaning script:** `Week1_Data_Collection_Cleaning_EDA/cleaning/clean_superstore_data.py`
- **Cleaned output:** `data/processed/cleaned_superstore.csv`
- **Original dataset:** 10,194 rows × 21 columns
- **Cleaned dataset:** 10,194 rows × 21 columns

The raw source file was not modified. All cleaning operations were performed on a separate DataFrame copy.

## 3. Cleaning Operations

### Date standardization
- Converted `Order Date` and `Ship Date` to datetime values.
- Used strict date parsing to prevent invalid date values from passing silently.

### Text standardization
- Removed leading and trailing whitespace from applicable text columns.
- Preserved original capitalization, names, identifiers, and source labels.

### Categorical values
Inspected and retained the existing values in:
- Ship Mode
- Segment
- Country/Region
- Region
- Category
- Sub-Category

No unnecessary category renaming was performed.

### Postal Code handling
- Converted Postal Code to string format.
- Preserved numeric and alphanumeric postal codes as text.
- Excluded Postal Code from general text cleaning before handling it separately.

### Data integrity
- Preserved the original row count and column structure.
- Checked numeric fields for unintended changes.
- Checked Row ID uniqueness and duplicate records.
- Verified that Ship Date is not earlier than Order Date.

## 4. Validation Results

| Validation | Result |
|---|---:|
| Original row count | 10,194 |
| Cleaned row count | 10,194 |
| Original column count | 21 |
| Cleaned column count | 21 |
| Unique orders | 5,111 |
| Duplicate rows | 0 |
| Missing values | 0 |
| Missing postal codes | 0 |
| Postal Code format | String |
| Invalid date ordering | 0 |
| Numeric field preservation | Passed |
| Export structure validation | Passed |
| Export validation | PASSED |

## 5. Date Coverage

- **Order Date:** 2023-01-03 to 2026-12-30
- **Ship Date:** 2023-01-07 to 2027-01-05

## 6. Export Details

The cleaned dataset was exported as a UTF-8 CSV file without a DataFrame index.

- **File:** `data/processed/cleaned_superstore.csv`
- **File size:** 2,472,638 bytes
- **Rows:** 10,194
- **Columns:** 21

The exported CSV was read back into Pandas and checked against the cleaned DataFrame. The validation passed.

## 7. Conclusion

Day 5 data cleaning and final dataset export were completed successfully. A reusable Python script was created, the cleaned dataset was exported, and the output passed the implemented validation checks.

The original raw dataset remains unchanged.
