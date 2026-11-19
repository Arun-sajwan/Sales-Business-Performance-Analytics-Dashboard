from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = PROJECT_ROOT / "data/raw/sample_-_superstore.xls"
OUTPUT_PATH = PROJECT_ROOT / "data/processed/cleaned_superstore.csv"

DATE_COLUMNS = ["Order Date", "Ship Date"]
POSTAL_COLUMN = "Postal Code"

CATEGORY_COLUMNS = [
    "Ship Mode",
    "Segment",
    "Country/Region",
    "Region",
    "Category",
    "Sub-Category",
]


def clean_dataset(source_path: Path) -> pd.DataFrame:
    """Load and clean the original Superstore dataset."""

    if not source_path.exists():
        raise FileNotFoundError(f"Source dataset not found: {source_path}")

    original = pd.read_excel(source_path, engine="xlrd")
    cleaned = original.copy()

    expected_rows, expected_columns = original.shape

    # Standardize date columns.
    for column in DATE_COLUMNS:
        cleaned[column] = pd.to_datetime(cleaned[column], errors="raise")

    # Trim whitespace from text fields, excluding Postal Code.
    text_columns = [
        column
        for column in cleaned.select_dtypes(
            include=["object", "str", "string"]
        ).columns
        if column != POSTAL_COLUMN
    ]

    for column in text_columns:
        cleaned[column] = cleaned[column].astype("string").str.strip()

    # Preserve postal codes as text identifiers.
    cleaned[POSTAL_COLUMN] = (
        cleaned[POSTAL_COLUMN].astype("string").str.strip()
    )

    # Validate the cleaned dataset.
    assert cleaned.shape == (expected_rows, expected_columns)
    assert cleaned.columns.tolist() == original.columns.tolist()
    assert not cleaned.isna().any().any(), "Unexpected missing values found."
    assert not cleaned.duplicated().any(), "Duplicate rows found."
    assert cleaned["Row ID"].is_unique, "Duplicate Row IDs found."
    assert (
        cleaned["Ship Date"] >= cleaned["Order Date"]
    ).all(), "Ship Date before Order Date found."
    assert cleaned[POSTAL_COLUMN].notna().all()

    # Ensure numeric source values remain unchanged.
    for column in ["Sales", "Quantity", "Discount", "Profit"]:
        pd.testing.assert_series_equal(
            cleaned[column],
            original[column],
            check_names=True,
        )

    # Confirm category labels were not unnecessarily changed.
    for column in CATEGORY_COLUMNS:
        assert set(cleaned[column].dropna()) == set(
            original[column].dropna()
        )

    # Confirm text fields have no leading/trailing whitespace.
    for column in text_columns:
        values = cleaned[column].dropna()
        assert values.eq(values.str.strip()).all()

    return cleaned


def export_and_validate(cleaned: pd.DataFrame) -> None:
    """Export the cleaned dataset and verify the CSV."""

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    cleaned.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8",
        date_format="%Y-%m-%d",
    )

    exported = pd.read_csv(
        OUTPUT_PATH,
        dtype={POSTAL_COLUMN: "string"},
        parse_dates=DATE_COLUMNS,
    )

    assert exported.shape == cleaned.shape
    assert exported.columns.tolist() == cleaned.columns.tolist()
    assert exported[POSTAL_COLUMN].equals(cleaned[POSTAL_COLUMN])
    assert exported["Row ID"].equals(cleaned["Row ID"])
    assert exported["Order ID"].astype("string").equals(cleaned["Order ID"].astype("string"))
    assert exported[DATE_COLUMNS].equals(cleaned[DATE_COLUMNS])

    for column in ["Sales", "Quantity", "Discount", "Profit"]:
        pd.testing.assert_series_equal(
            exported[column],
            cleaned[column],
            check_names=True,
            check_dtype=False,
        )

    print("\nDAY 5 CLEANING COMPLETED")
    print("-" * 40)
    print("Output:", OUTPUT_PATH.relative_to(PROJECT_ROOT))
    print("Rows:", len(exported))
    print("Columns:", len(exported.columns))
    print("Unique orders:", exported["Order ID"].nunique())
    print("Duplicate rows:", exported.duplicated().sum())
    print("Missing values:", exported.isna().sum().sum())
    print("Missing postal codes:", exported[POSTAL_COLUMN].isna().sum())
    print("Order date range:",
          exported["Order Date"].min().date(),
          "to", exported["Order Date"].max().date())
    print("Ship date range:",
          exported["Ship Date"].min().date(),
          "to", exported["Ship Date"].max().date())
    print("Postal Code dtype:", exported[POSTAL_COLUMN].dtype)
    print("Export size:", f"{OUTPUT_PATH.stat().st_size:,}", "bytes")
    print("Export validation: PASSED")


def main() -> None:
    original = pd.read_excel(SOURCE_PATH, engine="xlrd")
    cleaned = clean_dataset(SOURCE_PATH)

    print("Original dataset shape:", original.shape)
    print("Cleaned dataset shape:", cleaned.shape)
    print("Raw source file remains unchanged.")

    export_and_validate(cleaned)


if __name__ == "__main__":
    main()
