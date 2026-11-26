# Day 11 — Date Coverage and Missing Reporting Periods

## 1. Objective

Validate the date coverage of the cleaned Superstore dataset using `Order Date` and `Ship Date`. Identify missing or invalid date values, dates without recorded activity, reporting-period gaps, and partial boundary months.

The analysis uses the cleaned dataset without modifying the source or processed data.

## 2. Dataset scope

- Dataset: `data/processed/cleaned_superstore.csv`
- Total records: 10,194
- Unique orders: 5,111
- Date fields evaluated: `Order Date`, `Ship Date`
- Analysis periods: daily, monthly, quarterly, and yearly

Monthly, quarterly, and yearly activity counts represent dataset rows, not distinct orders.

## 3. Key findings

### Finding 1 — No missing or invalid date values

**Observation:** Both date fields contain complete and parseable date values across all 10,194 records.

**Evidence:**
- Order Date: 0 missing values and 0 invalid or unparseable values.
- Ship Date: 0 missing values and 0 invalid or unparseable values.
- Order Date range: 2023-01-03 to 2026-12-30.
- Ship Date range: 2023-01-07 to 2027-01-05.

**Business implication:** The dataset's date fields are complete for the records included in this analysis. This supports date-based grouping and trend analysis without excluding records due to missing or invalid dates.

**Limitation:** This validates the date values present in the dataset. It does not establish whether transactions that should have existed but are absent from the dataset were omitted.

### Finding 2 — Some individual calendar dates have no recorded activity

**Observation:** There are calendar dates within the observed date ranges on which no records appear.

**Evidence:**
- Order Date: 1,458 calendar days, of which 1,242 have activity and 216 have no recorded activity.
- Ship Date: 1,460 calendar days, of which 1,338 have activity and 122 have no recorded activity.
- Combined inactive date-field observations: 338.

**Business implication:** Daily reporting should distinguish dates with zero recorded activity from dates with missing date values. These inactive dates may be relevant when interpreting daily trends and chart continuity.

**Limitation:** The dataset does not provide an independent expected transaction calendar. Therefore, an inactive date cannot be classified as a data gap, operational shutdown, or missing transaction solely from this analysis.

### Finding 3 — No missing monthly, quarterly, or yearly reporting periods

**Observation:** Every monthly, quarterly, and yearly period within the observed date range contains at least one record for both date fields.

**Evidence:**

| Date field | Period | Periods in range | Periods with activity | Periods without activity |
|---|---|---:|---:|---:|
| Order Date | Monthly | 48 | 48 | 0 |
| Order Date | Quarterly | 16 | 16 | 0 |
| Order Date | Yearly | 4 | 4 | 0 |
| Ship Date | Monthly | 49 | 49 | 0 |
| Ship Date | Quarterly | 17 | 17 | 0 |
| Ship Date | Yearly | 5 | 5 | 0 |

**Business implication:** The dataset provides continuous monthly, quarterly, and yearly period coverage across the observed date ranges. These periods can be used for higher-level trend comparisons without an observed zero-activity reporting period.

**Limitation:** Having at least one record in every reporting period does not prove that every expected transaction is present or that the dataset is complete relative to an external business system.

### Finding 4 — First and last observed months are partial

**Observation:** The first and last calendar months in each date field's observed range do not cover the full calendar month.

**Evidence:**
- Order Date: first month January 2023, beginning with January 3; last month December 2026, ending with December 30.
- Ship Date: first month January 2023, beginning with January 7; last month January 2027, ending with January 5.

**Business implication:** Monthly comparisons should account for partial boundary months. Treating these periods as complete months could distort comparisons with full months.

**Limitation:** The date ranges show the first and last observed dates, not the intended reporting start and end dates. The analysis cannot establish whether records before or after these dates were expected.

### Finding 5 — Order Date and Ship Date have different coverage ranges

**Observation:** Ship Date coverage begins later than Order Date coverage and extends into January 2027.

**Evidence:**
- Order Date: January 3, 2023 to December 30, 2026.
- Ship Date: January 7, 2023 to January 5, 2027.
- Order Date has 48 observed months; Ship Date has 49 observed months.

**Business implication:** Reports using order and shipping dates should select the appropriate date field for the business question. Their reporting-period ranges should not be assumed to match.

**Limitation:** This comparison describes the recorded dates. It does not independently validate shipping performance, delivery completion, or expected shipping lead times.

## 4. Validation summary

| Validation | Result |
|---|---|
| Order Date missing values | PASS — 0 |
| Order Date invalid values | PASS — 0 |
| Ship Date missing values | PASS — 0 |
| Ship Date invalid values | PASS — 0 |
| Daily coverage generated for both date fields | PASS |
| Monthly coverage gaps | PASS — none |
| Quarterly coverage gaps | PASS — none |
| Yearly coverage gaps | PASS — none |
| Partial boundary months identified | PASS |
| Notebook and script outputs cross-validated | PASS |

## 5. Deliverables

- `notebooks/Day_11_Date_Coverage_and_Missing_Reporting_Periods.ipynb`
- `scripts/day_11_date_coverage_analysis.py`
- `visualizations/Day_11_Daily_Date_Coverage.csv`
- `visualizations/Day_11_Reporting_Period_Coverage.csv`
- `visualizations/Day_11_Date_Coverage_Summary.csv`
- `visualizations/Day_11_Monthly_Date_Coverage.png`
- `findings/Day_11_Date_Coverage_and_Missing_Reporting_Periods_Report.md`

## 6. Conclusion

The cleaned dataset contains no missing or invalid values in either date field. Individual dates without recorded activity exist, but they should not be interpreted as missing data without an independent expected transaction calendar. All observed monthly, quarterly, and yearly reporting periods contain activity. The first and last observed months are partial and should be treated carefully in period-over-period comparisons.

The notebook executed successfully, all 10 code cells completed without errors, and its results were cross-validated against the script-generated output files.
