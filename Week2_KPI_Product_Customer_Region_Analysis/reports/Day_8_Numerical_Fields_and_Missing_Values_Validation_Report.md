# Day 8: Numerical Fields and Missing Values Validation Report

## 1. Objective

The objective of this analysis was to validate the numerical fields and missing values in the cleaned Superstore dataset. The analysis examined data completeness, numerical ranges, invalid values, identifier fields, and potential statistical outliers.

## 2. Dataset Overview

- Source: `data/processed/cleaned_superstore.csv`
- Total records: 10,194
- Total columns: 21
- Total cells: 214,074
- Numerical fields examined: Row ID, Sales, Quantity, Discount, Profit

The Postal Code field was loaded as text to preserve its identifier characteristics. Order ID, Customer ID, and Product ID were also treated as identifiers rather than numerical measures.

## 3. Missing-Value Analysis

The missing-value analysis covered all 21 columns.

| Metric | Result |
|---|---:|
| Total missing cells | 0 |
| Columns containing missing values | 0 |
| Rows containing missing values | 0 |
| Fully populated rows | 10,194 |
| Overall missing percentage | 0.00% |

**Finding:** All 10,194 records are fully populated across all 21 columns. No missing-value treatment was required.

## 4. Numerical Field Validation

### 4.1 Numerical Summary

| Field | Minimum | Maximum | Mean | Missing | Zero | Negative |
|---|---:|---:|---:|---:|---:|---:|
| Row ID | 1 | 10,194 | 5,097.500 | 0 | 0 | 0 |
| Sales | 0.444 | 22,638.480 | 228.226 | 0 | 0 | 0 |
| Quantity | 1 | 14 | 3.792 | 0 | 0 | 0 |
| Discount | 0.000 | 0.800 | 0.155 | 0 | 4,925 | 0 |
| Profit | -6,599.978 | 8,399.976 | 28.673 | 0 | 65 | 1,901 |

### 4.2 Sales

- Negative sales records: 0
- Zero sales records: 0
- Minimum sales: 0.444
- Maximum sales: 22,638.480

**Finding:** All Sales values are positive and finite.

### 4.3 Quantity

- Negative quantity records: 0
- Zero quantity records: 0
- Non-integer quantity records: 0
- Minimum quantity: 1
- Maximum quantity: 14

**Finding:** All Quantity values are positive integers.

### 4.4 Discount

- Negative discount records: 0
- Discount values above 1 (100%): 0
- Zero discount records: 4,925
- Minimum discount: 0.00
- Maximum discount: 0.80

**Finding:** All Discount values are within the expected range of 0 to 1. Zero discount is a valid observation.

### 4.5 Profit

- Negative profit records: 1,901
- Zero profit records: 65
- Positive profit records: 8,228
- Minimum profit: -6,599.978
- Maximum profit: 8,399.976

**Finding:** Negative Profit values represent loss-making records and are retained as valid business observations. They are not automatically classified as data errors.

## 5. Identifier and Data-Type Validation

| Field | Data Type | Treatment |
|---|---|---|
| Row ID | Integer | Unique row identifier |
| Order ID | String | Order identifier |
| Customer ID | String | Customer identifier |
| Product ID | String | Product identifier |
| Postal Code | String | Geographic identifier |

Row ID validation:

- Unique Row IDs: 10,194
- Expected records: 10,194
- Minimum Row ID: 1
- Maximum Row ID: 10,194
- Duplicate Row IDs: 0
- Continuous sequence: Valid

**Finding:** Row IDs are unique and form a continuous sequence from 1 to 10,194. Identifier fields are treated as identifiers rather than measures.

## 6. Potential Outlier Analysis

The Interquartile Range (IQR) method was applied to Sales, Quantity, and Profit.

The outlier boundaries were calculated using:

- Lower bound = Q1 - 1.5 × IQR
- Upper bound = Q3 + 1.5 × IQR

| Field | Lower Bound | Upper Bound | Outlier Count | Percentage |
|---|---:|---:|---:|---:|
| Sales | -271.200 | 497.920 | 1,183 | 11.60% |
| Quantity | -2.500 | 9.500 | 175 | 1.72% |
| Profit | -39.545 | 70.604 | 1,913 | 18.77% |

**Interpretation:**

- Sales outliers may represent unusually high-value transactions.
- Quantity outliers represent records with quantities above the statistical upper boundary.
- Profit outliers may represent unusually high profits or losses.

These values are statistical flags, not proof of incorrect records. No outliers were removed or modified during this validation.

## 7. Final Validation Results

| Validation Check | Result |
|---|---|
| Dataset contains 21 columns | PASS |
| No missing values | PASS |
| All numerical values are finite | PASS |
| Sales values are non-negative | PASS |
| Quantity values are positive | PASS |
| Quantity values are integers | PASS |
| Discount values are between 0 and 1 | PASS |
| Row IDs are unique | PASS |
| Row IDs form a continuous sequence | PASS |
| Postal Code is stored as text | PASS |

**Total checks passed: 10/10**

## 8. Conclusion

The cleaned Superstore dataset passed all 10 validation checks.

The dataset contains 10,194 records and 21 columns, with no missing values or infinite numerical values. Sales, Quantity, and Discount satisfy the applied validation rules. Row IDs are unique and continuous, and identifier fields are represented using appropriate text data types.

Negative Profit values are retained because they represent business losses. Potential statistical outliers were identified for further analytical awareness but were not treated as confirmed data errors.

No records were removed or modified as part of this validation.

## 9. Deliverable

- Notebook: `Week2_KPI_Product_Customer_Region_Analysis/notebooks/Day_8_Numerical_Fields_and_Missing_Values_Validation.ipynb`
- Report: `Week2_KPI_Product_Customer_Region_Analysis/reports/Day_8_Numerical_Fields_and_Missing_Values_Validation_Report.md`
