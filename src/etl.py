from pathlib import Path

import pandas as pd


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Local data directory
DATA_DIR = PROJECT_ROOT / "data"


def load_csv(file_path: str | Path) -> pd.DataFrame:
    """Load a CSV file and display basic information."""

    file_path = Path(file_path)

    if not file_path.is_absolute():
        file_path = PROJECT_ROOT / file_path

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}\n"
            "Check that the dataset exists inside the project."
        )

    df = pd.read_csv(file_path, low_memory=False)

    print(f"\nLoaded file: {file_path.name}")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    return df


def inspect_data(df: pd.DataFrame) -> None:
    """Display a basic data quality report."""

    print("\n--- Column names and data types ---")
    print(df.dtypes)

    print("\n--- Missing values ---")
    print(df.isnull().sum())

    print("\n--- Duplicate rows ---")
    print(df.duplicated().sum())

    print("\n--- First five rows ---")
    print(df.head())


def main() -> None:
    """Load and inspect the SKU datasets."""

    inventory_file = DATA_DIR / "sku_inventory_flags.csv"
    master_file = DATA_DIR / "sku_master.csv"

    for file_path in [inventory_file, master_file]:
        try:
            df = load_csv(file_path)
            inspect_data(df)

        except FileNotFoundError as error:
            print(f"\nWARNING: {error}")


if __name__ == "__main__":
    main()
