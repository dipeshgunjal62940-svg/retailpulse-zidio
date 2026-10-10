from pathlib import Path

import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def load_data(file_path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset and return it as a DataFrame."""
    file_path = Path(file_path)

    if not file_path.is_absolute():
        file_path = PROJECT_ROOT / file_path

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path)

    print(f"Dataset loaded successfully: {file_path.name}")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    return df


def main():
    # Place your dataset inside the local data/ folder.
    file_path = DATA_DIR / "retail_transactions.csv"

    try:
        df = load_data(file_path)
        print("\nFirst five rows:")
        print(df.head())

        print("\nMissing values by column:")
        print(df.isnull().sum())

    except FileNotFoundError as error:
        print(error)
        print("Please place the dataset in the local data/ folder.")


if __name__ == "__main__":
    main()
