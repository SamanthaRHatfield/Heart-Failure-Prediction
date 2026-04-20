from pathlib import Path
import pandas as pd

"""Load the dataset from a CSV file."""
def load_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)

"""Print basic dataset information."""
def inspect_data(df: pd.DataFrame) -> None:
    print("\n--- First 5 Rows ---")
    print(df.head())

    print("\n--- Dataset Shape ---")
    print(df.shape)

    print("\n--- Column Names ---")
    print(df.columns.tolist())

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Target Distribution ---")
    print(df["HeartDisease"].value_counts())

"""Split dataframe into features, target, and identify column types."""
def split_features_target(
    df: pd.DataFrame, target_col: str
) -> tuple[pd.DataFrame, pd.Series, list[str], list[str]]:
    X = df.drop(columns=[target_col])
    y = df[target_col]

    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
    numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

    print("\n--- Categorical Columns ---")
    print(categorical_cols)

    print("\n--- Numeric Columns ---")
    print(numeric_cols)

    return X, y, categorical_cols, numeric_cols