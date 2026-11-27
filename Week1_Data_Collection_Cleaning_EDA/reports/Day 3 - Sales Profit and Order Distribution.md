# Day 3 – Explore Sales, Profit, and Order Distributions

## Project
**Sales and Business Performance Analytics Dashboard**

## 1. Objective

The objective of this task is to explore Sales, Profit, and Order distributions to understand business performance, identify trends, and analyze category-wise and region-wise performance.

## 2. Dataset Overview

- **Dataset Name:** Sample - Superstore
- **Total Records:** 10,194
- **Total Columns:** 21
- **Unique Orders:** 5,111
- **Unique Customers:** 804

## 3. Sales Distribution Analysis

Analyzed Sales using descriptive statistics.

| Metric | Value |
|---|---:|
| Count | 10,194 |
| Mean | 228.23 |
| Standard Deviation | 619.91 |
| Minimum | 0.444 |
| 25% | 17.22 |
| Median | 53.91 |
| 75% | 209.50 |
| Maximum | 22,638.48 |

### Observations
- Average sales are higher than median sales.
- Sales values show a positively skewed distribution.
- Some records have very high sales values.
- Sales values vary significantly across records.

## 4. Profit Distribution Analysis

Analyzed Profit using descriptive statistics.

| Metric | Value |
|---|---:|
| Count | 10,194 |
| Mean | 28.67 |
| Standard Deviation | 232.47 |
| Minimum | -6,599.98 |
| 25% | 1.76 |
| Median | 8.69 |
| 75% | 29.30 |
| Maximum | 8,399.98 |

### Observations
- The dataset contains both positive and negative profit values.
- Some records show significant losses.
- Average profit is higher than median profit.
- Profit values show considerable variation.

## 5. Order Distribution Analysis

Analyzed order-level Sales and Profit by grouping records using Order ID.

- **Total Unique Orders:** 5,111

### Order-Level Statistics

| Metric | Sales | Profit |
|---|---:|---:|
| Count | 5,111 | 5,111 |
| Mean | 455.20 | 57.19 |
| Standard Deviation | 949.79 | 342.23 |
| Minimum | 0.556 | -6,892.37 |
| Median | 149.20 | 16.24 |
| Maximum | 23,661.23 | 8,762.39 |

### Observations
- Average order value is 455.20.
- Median order value is 149.20.
- Some orders have negative total profit.
- Order values show considerable variation.

## 6. Category-wise Sales and Profit Analysis

Analyzed total Sales, Profit, and unique Orders for each product category.

| Category | Sales | Profit | Total Orders |
|---|---:|---:|---:|
| Furniture | 754,747.76 | 19,730.00 | 1,819 |
| Office Supplies | 731,893.31 | 126,023.44 | 3,812 |
| Technology | 839,893.28 | 146,543.38 | 1,560 |

### Observations
- Technology has the highest sales.
- Technology generates the highest profit.
- Office Supplies has the highest number of unique orders.
- Furniture generates comparatively lower profit despite having high sales.

## 7. Region-wise Sales and Profit Analysis

Analyzed Sales, Profit, and unique Orders across four regions.

| Region | Sales | Profit | Total Orders |
|---|---:|---:|---:|
| Central | 503,170.67 | 39,865.31 | 1,179 |
| East | 691,828.17 | 94,883.26 | 1,475 |
| South | 391,721.91 | 46,749.43 | 822 |
| West | 739,813.61 | 110,798.82 | 1,635 |

### Observations
- West region has the highest sales and profit.
- East region has the second-highest sales and profit.
- South region has the lowest sales.
- West region also has the highest number of unique orders.

## 8. Monthly Sales and Order Trend Analysis

Analyzed monthly Sales, Profit, and Order counts using Order Date.

### Monthly Order Trend – Observations
- The monthly order trend shows an overall increasing pattern.
- Order counts
