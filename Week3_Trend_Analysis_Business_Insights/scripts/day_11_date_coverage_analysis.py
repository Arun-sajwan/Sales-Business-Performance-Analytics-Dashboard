from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = ROOT / "data" / "processed" / "cleaned_superstore.csv"
OUTPUT_DIR = ROOT / "Week3_Trend_Analysis_Business_Insights" / "visualizations"

DATE_COLUMNS = ["Order Date", "Ship Date"]
PERIODS = {
    "daily": "D",
    "monthly": "M",
    "quarterly": "Q",
    "yearly": "Y",
}


def load_data():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE, dtype={"Postal Code": "string"})

    required = ["Order ID", *DATE_COLUMNS]
    missing_columns = [col for col in required if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Required columns are missing: {missing_columns}")

    for col in DATE_COLUMNS:
        df[f"_{col}_raw"] = df[col].copy()
        df[col] = pd.to_datetime(
            df[col], format="%Y-%m-%d", errors="coerce"
        )

    return df


def analyze_date_column(df, date_column):
    dates = df[date_column]
    valid = dates.dropna()

    if valid.empty:
        raise ValueError(f"No valid dates found in {date_column}")

    first_date = valid.min().normalize()
    last_date = valid.max().normalize()

    daily_counts = (
        df.dropna(subset=[date_column])
        .assign(_date=lambda x: x[date_column].dt.normalize())
        .groupby("_date")
        .agg(
            row_count=("Order ID", "size"),
            unique_orders=("Order ID", "nunique"),
        )
    )

    daily_calendar = pd.date_range(first_date, last_date, freq="D")
    daily = daily_counts.reindex(daily_calendar, fill_value=0)
    daily.index.name = "date"
    daily = daily.reset_index()
    daily.insert(0, "date_column", date_column)
    daily["has_activity"] = daily["row_count"] > 0

    period_tables = []
    raw_dates = df[f"_{date_column}_raw"]
    blank_dates = raw_dates.isna() | (
        raw_dates.astype("string").str.strip().eq("").fillna(False)
    )
    invalid_dates = (~blank_dates) & dates.isna()

    summary = {
        "date_column": date_column,
        "total_rows": len(df),
        "missing_date_values": int(blank_dates.sum()),
        "invalid_or_unparseable_dates": int(invalid_dates.sum()),
        "minimum_date": first_date.date().isoformat(),
        "maximum_date": last_date.date().isoformat(),
        "distinct_active_dates": int(valid.dt.normalize().nunique()),
        "calendar_days_in_range": len(daily_calendar),
        "days_with_activity": int(daily["has_activity"].sum()),
        "days_without_activity": int((~daily["has_activity"]).sum()),
    }

    for period_name, frequency in PERIODS.items():
        period_values = dates.dropna().dt.to_period(frequency)
        counts = period_values.value_counts().sort_index()

        calendar = pd.period_range(
            start=period_values.min(),
            end=period_values.max(),
            freq=frequency,
        )
        complete = counts.reindex(calendar, fill_value=0)

        table = pd.DataFrame({
            "date_column": date_column,
            "period_type": period_name,
            "period": complete.index.astype(str),
            "row_count": complete.values,
        })
        table["has_activity"] = table["row_count"] > 0

        # Mark boundary periods whose observed dates do not span
        # the complete calendar period. This is not a data-loss test.
        if period_name == "daily":
            table["boundary_period"] = False
        else:
            first_period = period_values.min()
            last_period = period_values.max()
            table["boundary_period"] = table["period"].isin(
                [str(first_period), str(last_period)]
            )

        period_tables.append(table)

        summary[f"{period_name}_periods_in_range"] = len(calendar)
        summary[f"{period_name}_periods_with_activity"] = int(
            (complete > 0).sum()
        )
        summary[f"{period_name}_periods_without_activity"] = int(
            (complete == 0).sum()
        )

    # Calendar-boundary completeness for the first and last months.
    first_month = valid.min().to_period("M")
    last_month = valid.max().to_period("M")
    summary["first_month"] = str(first_month)
    summary["first_month_first_observed_date"] = valid.min().date().isoformat()
    summary["first_month_calendar_start"] = first_month.start_time.date().isoformat()
    summary["first_month_partial_observation"] = (
        valid.min().normalize() > first_month.start_time.normalize()
    )
    summary["last_month"] = str(last_month)
    summary["last_month_last_observed_date"] = valid.max().date().isoformat()
    summary["last_month_calendar_end"] = last_month.end_time.date().isoformat()
    summary["last_month_partial_observation"] = (
        valid.max().normalize() < last_month.end_time.normalize()
    )

    return daily, pd.concat(period_tables, ignore_index=True), summary


def create_monthly_chart(period_coverage):
    monthly = period_coverage[
        period_coverage["period_type"] == "monthly"
    ].copy()

    pivot = monthly.pivot(
        index="period",
        columns="date_column",
        values="row_count",
    )

    ax = pivot.plot(
        kind="line",
        marker="o",
        figsize=(14, 6),
        linewidth=1.8,
    )
    ax.set_title("Monthly Record Activity: Order Date vs Ship Date")
    ax.set_xlabel("Reporting month")
    ax.set_ylabel("Dataset rows")
    ax.grid(True, alpha=0.3)
    ax.legend(title="Date field")
    plt.xticks(rotation=60, ha="right")
    plt.tight_layout()

    chart_path = OUTPUT_DIR / "Day_11_Monthly_Date_Coverage.png"
    plt.savefig(chart_path, dpi=160)
    plt.close()
    return chart_path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = load_data()

    daily_tables = []
    period_tables = []
    summaries = []

    for date_column in DATE_COLUMNS:
        daily, periods, summary = analyze_date_column(df, date_column)
        daily_tables.append(daily)
        period_tables.append(periods)
        summaries.append(summary)

    daily_output = pd.concat(daily_tables, ignore_index=True)
    period_output = pd.concat(period_tables, ignore_index=True)
    summary_output = pd.DataFrame(summaries)

    daily_path = OUTPUT_DIR / "Day_11_Daily_Date_Coverage.csv"
    period_path = OUTPUT_DIR / "Day_11_Reporting_Period_Coverage.csv"
    summary_path = OUTPUT_DIR / "Day_11_Date_Coverage_Summary.csv"

    daily_output.to_csv(daily_path, index=False)
    period_output.to_csv(period_path, index=False)
    summary_output.to_csv(summary_path, index=False)

    chart_path = create_monthly_chart(period_output)

    print("=" * 72)
    print("DAY 11 — DATE COVERAGE AND REPORTING PERIOD ANALYSIS")
    print("=" * 72)
    print("Dataset shape:", df.shape)
    print("Unique orders:", df["Order ID"].nunique())
    print("\nDATE COVERAGE SUMMARY")
    print(summary_output.to_string(index=False))
    print("\nDATES WITHOUT RECORDED ACTIVITY")
    inactive_days = daily_output[~daily_output["has_activity"]]
    if inactive_days.empty:
        print("None.")
    else:
        print("Inactive calendar days:", len(inactive_days))
        print(inactive_days.groupby("date_column").size().to_string())
        print("First 10 examples:")
        print(inactive_days.head(10).to_string(index=False))

    print("\nMISSING REPORTING PERIODS (MONTHLY / QUARTERLY / YEARLY)")
    reporting_periods = period_output[
        period_output["period_type"].isin(["monthly", "quarterly", "yearly"])
    ]
    missing_periods = reporting_periods[~reporting_periods["has_activity"]]
    if missing_periods.empty:
        print("None. Every monthly, quarterly, and yearly period has activity.")
    else:
        print(missing_periods.to_string(index=False))

    print("\nOUTPUT FILES")
    for path in [daily_path, period_path, summary_path, chart_path]:
        print(f"{path.relative_to(ROOT)} ({path.stat().st_size:,} bytes)")

    print("\nINTERPRETATION")
    print(
        "Dates with zero recorded activity are not automatically classified "
        "as missing data. Reporting-period coverage only confirms that at "
        "least one row exists in each period within the observed range."
    )
    print("=" * 72)


if __name__ == "__main__":
    main()
