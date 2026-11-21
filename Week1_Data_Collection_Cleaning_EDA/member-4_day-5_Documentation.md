# Week 1: Data Collection, Cleaning & Exploratory Data Analysis (EDA)

## Objective

The goal of Week 1 was to prepare a reliable and analysis-ready dataset by collecting data, assessing its quality, performing cleaning operations, and conducting exploratory data analysis (EDA).

---

## Tasks Completed

### Day 1: Repository Creation and Business Understanding

- initialize github Repository.
- Defined project objectives.
- Identified business problems and key analysis questions.
- Determined expected outcomes and KPIs.

### Day 2: Data Collection and Data Dictionary Creation

- Gathered dataset from the approved source.
- Verified dataset structure and available fields.
- Stored original files in the raw dataset folder.

- Documented all dataset columns.
- Defined data types and descriptions.
- Recorded assumptions and transformations.

### Day 3: Data Quality Assessment

- Checked dataset dimensions.
- Identified missing values.
- Examined duplicate records.
- Reviewed data types and column consistency.

### Day 4: Data Cleaning

- Removed duplicate records.
- Handled missing values.
- Standardized column names.
- Fixed inconsistent formats.
- Converted fields into appropriate data types.

### Day 5: Exploratory Data Analysis and Documentation (Summary & Findings)

Performed analysis on:

- Sales distribution
- Product performance
- Category analysis
- Regional performance
- Customer trends
- Outlier detection

- Documented major observations.
- Identified preliminary business insights.
- Prepared dataset for Week 2 KPI analysis.

---

## Important Week 1 Findings and Insights

### Dataset and Performance Overview

- The analysis dataset contains **10,194 transaction rows, 21 columns, 5,111 distinct orders, and 804 distinct customers**.
- Recorded sales are **$2.326 million**, with total profit of **$292,296.81** and an overall profit margin of approximately **12.56%**.
- The order-date range is **3 January 2023 to 30 December 2026**.
- The median shipping time is **4 days**, with an average of approximately **3.96 days**.
- Sales increased from **$494,040.21 in 2023** to **$745,567.53 in 2026**, indicating a strong positive growth trend across the period.

### Data Quality Findings

- No missing values or fully duplicated rows were found in the 21-column dataset.
- The source contains valid sales, quantity, discount, and profit values.
- **1,901 transaction rows (18.65%)** have negative profit, totaling **-$157,038.93** in losses.
- `Order ID` is repeated because an order can contain multiple product line items. Orders should be counted using distinct `Order ID` values rather than row count.
- Negative profit values are valid observed business outcomes and were retained for analysis.

### Category Insights

- **Technology** is the strongest-performing category, generating **$839,893.28 in sales** and **$146,543.38 in profit**, with a **17.45% profit margin**.
- **Office Supplies** generated **$731,893.31 in sales** and **$126,023.44 in profit**, with a **17.22% margin**.
- **Furniture** generated **$754,747.76 in sales** but the lowest margin of the three categories at **2.61%**, with only **$19,730.00 in profit**.
- Copiers, Accessories, and Phones are the major sub-category profit drivers. Copiers have the strongest sub-category margin at approximately **37.21%**.
- Tables are a key loss area, with **-$17,753.21 in profit** and a margin of approximately **-8.53%**.

### Regional Insights

- The **West** region leads with **$739,813.61 in sales**, **$110,798.82 in profit**, and a **14.98% profit margin**.
- The **East** region is the second-largest market by sales at **$691,828.17** and achieved a **13.71% margin**.
- The **Central** region is the weakest margin region at **7.92%**, despite generating **$503,170.67 in sales**.
- The **South** region generated **$391,721.91 in sales** with an **11.93% margin**.

### Customer and Segment Insights

- The **Consumer** segment contributes the highest sales at **$1.171 million** and 416 customers, but its margin is lower than the Corporate and Home Office segments.
- **Corporate** contributes **$715.806 thousand in sales** with a **13.17% margin**.
- **Home Office** has the strongest segment margin at **14.02%**, with **$440.068 thousand in sales**.
- Sean Miller is the highest-sales customer at **$25,043.05**, but generated a negative profit of **-$1,980.74**.
- Tamara Chand is a high-value profitable customer, with **$19,052.22 in sales** and **$8,981.32 in profit**.

### Discount and Product Insights

- Orders with no discount generate a **29.56% profit margin**.
- Profit margins decline sharply as discounts increase: 20% discount sales have an **11.77% margin**, while 30% discount sales become loss-making at approximately **-10.06%**.
- Every recorded transaction at **50% to 80% discount** is loss-making.
- The **Canon imageCLASS 2200 Advanced Copier** is the top-revenue product at **$61,599.82 in sales** and also the top-profit product at **$25,199.93 in profit**.
- Several high-sales products, including the Cisco TelePresence System EX90 and GBC DocuBind P400, generated negative profit and require further pricing and discount review.

### Business Implications

- Preserve Technology and Office Supplies growth, especially Copiers, Accessories, Phones, and other high-margin sub-categories.
- Investigate Furniture and Central-region profitability, with priority focus on Tables, Bookcases, discounts, and operating costs.
- Introduce tighter discount controls above 30%, as these discounts are associated with losses.
- Review the product mix and pricing for loss-making products and loss-making customers before scaling sales.
- Use distinct `Order ID` values for order KPIs and row-level values for product-line analysis in Week 2.

---

## Deliverables

### 1. Cleaned Dataset

- Analysis-ready version of the original dataset.
- Location: [`data/processed/`](https://github.com/Arun-sajwan/Sales-Business-Performance-Analytics-Dashboard/blob/main/data/processed/)

### 2. Data Dictionary

- Documentation describing all columns and their purpose.
- Location: [`data_dictionary/Superstore_Initial_Data_Dictionary.xlsx`](https://github.com/Arun-sajwan/Sales-Business-Performance-Analytics-Dashboard/blob/main/Week1_Data_Collection_Cleaning_EDA/data_dictionary/Superstore_Initial_Data_Dictionary.xlsx).

### 3. Data Cleaning Report

- Summary of issues found and corrections applied.
- Location: [`cleaning/Member-4_Day-4_data_quality_documentation.md`](https://github.com/Arun-sajwan/Sales-Business-Performance-Analytics-Dashboard/blob/main/Week1_Data_Collection_Cleaning_EDA/cleaning/Member-4_Day-4_data_quality_documentation.md).

### 4. EDA Notebook

- Contains exploratory analysis and visualizations.
- [`notebooks/`](https://github.com/Arun-sajwan/Sales-Business-Performance-Analytics-Dashboard/tree/main/Week1_Data_Collection_Cleaning_EDA/notebooks)

### 5. Visual Assets

- Charts and graphs generated during EDA.
- Location: [`visualizations/Day 4 Visuals/`](https://github.com/Arun-sajwan/Sales-Business-Performance-Analytics-Dashboard/tree/main/Week1_Data_Collection_Cleaning_EDA/visualizations/Day%204%20Visuals)

---

## Key Data Quality Checks

- Missing value analysis
- Duplicate record detection
- Data type validation
- Null percentage calculation
- Outlier identification
- Consistency verification

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Week 1 Outcome

Successfully transformed raw data into a clean, structured dataset and generated initial business insights through exploratory analysis. The project is now ready for KPI calculation and detailed Product, Customer, and Regional Analysis in Week 2.

---

## Next Phase

➡ Week 2: KPI, Product, Customer & Region Analysis

Focus Areas:

- Total Sales
- Total Orders
- Customer Segmentation
- Product Performance
- Regional Comparison
- Business KPIs
