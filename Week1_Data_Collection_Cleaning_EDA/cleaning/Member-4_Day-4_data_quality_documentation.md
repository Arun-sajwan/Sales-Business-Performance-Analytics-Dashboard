# Data Quality Documentation

**Project:** Sales & Business Performance Analytics Dashboard\
**Prepared by:** Member 4 
**Week:** 1
**Review date:** 18 November 2026
**Status:** Draft -- requires confirmation from Member 1 (Data
Collection & Data Cleaning)

------------------------------------------------------------------------

## 1. Purpose

This document records data-quality issues identified in the sales
dataset, actions taken to address them, and assumptions or limitations
that may affect analysis and the dashboard.

## 2. Dataset details

  Item                Details
  ------------------- ---------------------------------------------
  Dataset name        Superstore sales sample
  Source              Tableau public sample data: [Tableau Superstore data](https://public.tableau.com/app/learn/sample-data)
  Original file       `sample_-_superstore.xls`
  Number of rows      10,194
  Number of columns   21
  Cleaned dataset     Not yet created
  Reviewed with       Member 1 -- Data Collection & Data Cleaning

## 3. Data-quality review

The source workbook was inspected on 18 November 2026. It contains the
`Orders`, `People`, and `Returns` worksheets; this review uses the
10,194-row `Orders` worksheet.

  ----------------------------------------------------------------------------------
  Area checked   What to inspect    Finding in     Action taken       Status
                                    this dataset                      
  -------------- ------------------ -------------- ------------------ --------------
  Missing values Blank/null cells   0 blank cells No treatment      Complete
                 and affected       in any of the  required\]         
                 21 columns                        

  Duplicate      Fully duplicated   0 fully       No rows removed;   Complete
  records        rows and possible  duplicated    repeated order IDs 
                 repeated order IDs rows; 5,111    are legitimate     
                                   distinct IDs   multi-line orders   
                                   with repeated   because 5,083      
                                   IDs             additional rows    
                                                   use an existing ID 

  Date           Mixed formats,     Both date      Excel datetime     Complete
  formatting     invalid dates, or  columns are    values retained;   
                 unparseable values valid          no conversion      
                                   datetime types  required            
                                   from 03 Jan     (0 ship dates      
                                   2023 to 30      before order      
                                   Dec 2026        dates)              

  Category       Variations in      No leading or  No cleaning         Complete
  consistency    product/category   trailing       required\]          
                 names, spelling,  whitespace or    
                 or whitespace     spelling            
                                   variations found   

  Invalid or     Unexpected         1,901 negative Retain negative     Complete
  unusual values negative           profit records; profit as observed;  
                 quantities,       Sales are       no negative Sales,  
                 prices, sales, or positive and     Quantity, or        
                 profits           Quantity >= 1;  Discount values      
                                   Discount is     found                  
                                   within 0%-80%                        

  Data types     Numeric/date       Types are       No conversion       Complete
                 fields stored as   appropriate:    required\]           
                 text or incorrect numeric for       
                 types             Sales, Quantity,     
                                   Discount and Profit;
                                   datetime for both   
                                   date columns        
  ----------------------------------------------------------------------------------

## 4. Detailed issue log

Add one entry for every issue confirmed by the data-cleaning team.

### Issue 1 -- Negative profit values

-   **Column(s) affected:** `Profit`
-   **What was found:** 1,901 of 10,194 rows have negative profit.
-   **How it was handled:** Retained without alteration; no records
    were deleted or profit values changed.
-   **Reason for the action:** Negative profit is a plausible and
    commonly recorded business outcome, and no evidence was found that
    these values are invalid.
-   **Validation performed:** Checked every numeric profit value and
    confirmed that sales and quantity remain valid in the affected rows.


### Issue 2 -- Repeated order IDs

-   **Column(s) affected:** `Order ID`
-   **What was found:** 5,111 distinct order IDs occur across 10,194 rows. 
                        5,083 rows repeat an existing order ID.
-   **How it was handled:** Retained all rows. 
                            no deduplication by order ID was performed.
-   **Reason for the action:** Each row is a distinct product line item
    and `Row ID` is unique, so repeated order IDs represent valid
    multi-line orders rather than duplicate records.
-   **Validation performed:** Confirmed `Row ID` has 10,194 unique
    values and no fully duplicated rows exist.


Missing values, date formatting, data types, discount ranges,
category-label consistency, duplicate records, and nonpositive sales or
quantity values were checked and found to require no cleaning in the
source workbook.

## 5. Cleaning decisions and assumptions

Recorded decisions that could affect analysis, such as:

-   Whether missing values were retained, removed, or filled, and why.
-   How duplicate rows were distinguished from legitimate multiple line
    items belonging to one order.
-   Which date format was selected.
-   How inconsistent category labels were standardized.
-   How returns, cancellations, negative values, and unusual
    transactions were treated.
-   Whether any records or columns were excluded from analysis.

**Decisions confirmed so far:** 10,194 source rows. 
    Treat negative profit values as observed business losses. Count orders using
    distinct `Order ID` values rather than row count. Retain the existing
    category labels.
    These decisions require final confirmation from Member1; 
    no cleaned dataset has been produced.

## 6. Files and repository locations

  -----------------------------------------------------------------------------------------------
  File                    Expected location                               Status
  ----------------------- ----------------------------------------------- -----------------------
  Original dataset        `data/raw/sample_-_superstore.xls`             Complete

  Cleaning script         Not yet created                                Pending

  Cleaned dataset         `data/interim/`                                Pending

  This documentation      `Week1_Data_Collection_Cleaning_EDA/cleaning/` 

  Draft                   `Member-4_Day-4_data_quality_documentation.md`
  -----------------------------------------------------------------------------------------------
## 8. Conclusion

This document records data-quality checks and cleaning decisions for the
Sales & Business Performance Analytics Dashboard. It remains a draft
until the findings, actions, and validation checks have been confirmed
against the actual dataset by Member 1.

