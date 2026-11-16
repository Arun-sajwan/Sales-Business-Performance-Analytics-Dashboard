# Day 2 – Data Inspection Report

**Project:** Sales & Business Performance Analytics Dashboard  
**Week:** 1 – Data Collection, Cleaning & EDA  
**Role:** Member 1 – Data Cleaning  
**Dataset:** Superstore (`sample_-_superstore.xls`)  
**Format:** Excel `.xls`

## 1. Objective

Load the original Superstore dataset using Pandas and inspect its dimensions, column names, data types, missing values, and sample records.

## 2. Tools and Libraries

- Python
- Pandas 3.0.5
- xlrd 2.0.2

## 3. Dataset Overview

| Metric | Result |
|---|---:|
| Total rows | 10,194 |
| Total columns | 21 |
| Total missing values | 0 |

## 4. Available Columns

1. Row ID
2. Order ID
3. Order Date
4. Ship Date
5. Ship Mode
6. Customer ID
7. Customer Name
8. Segment
9. Country/Region
10. City
11. State/Province
12. Postal Code
13. Region
14. Product ID
15. Category
16. Sub-Category
17. Product Name
18. Sales
19. Quantity
20. Discount
21. Profit

## 5. Data Types

| Column | Data Type |
|---|---|
| Row ID | int64 |
| Order ID | str |
| Order Date | datetime64[us] |
| Ship Date | datetime64[us] |
| Ship Mode | str |
| Customer ID | str |
| Customer Name | str |
| Segment | str |
| Country/Region | str |
| City | str |
| State/Province | str |
| Postal Code | object |
| Region | str |
| Product ID | str |
| Category | str |
| Sub-Category | str |
| Product Name | str |
| Sales | float64 |
| Quantity | int64 |
| Discount | float64 |
| Profit | float64 |

## 6. Missing Value Analysis

The inspection identified no missing values in any of the 21 columns.

| Metric | Result |
|---|---:|
| Columns with missing values | 0 |
| Total missing values | 0 |

## 7. Initial Observations

- Both Order Date and Ship Date were recognized as datetime values.
- Sales, Discount, and Profit were recognized as floating-point values.
- Quantity and Row ID were recognized as integer values.
- Postal Code was recognized as an object data type and should be reviewed during the cleaning stage.
- The dataset contains order, customer, product, shipping, geographic, and financial fields.

## 8. Conclusion

The initial inspection of the Superstore dataset was completed successfully using Pandas.

The dataset contains 10,194 rows and 21 columns, with no missing values detected.

No records were removed, no values were modified, and the original raw dataset was preserved.

**Scope note:** Duplicate detection, invalid-value checks, standardization, and data cleaning are reserved for subsequent project days.
