"""Customer churn data cleaning and feature engineering pipeline."""

from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
OUTPUT_DATA_PATH = BASE_DIR / "data" / "cleaned_data.csv"


def load_dataset(file_path=RAW_DATA_PATH):
    """Load the raw churn dataset."""
    return pd.read_csv(file_path)


def clean_dataset(dataframe):
    """Handle missing values and standardize data types."""
    cleaned_dataframe = dataframe.copy()

    cleaned_dataframe["TotalCharges"] = pd.to_numeric(
        cleaned_dataframe["TotalCharges"], errors="coerce"
    )
    cleaned_dataframe["TotalCharges"] = cleaned_dataframe["TotalCharges"].fillna(
        cleaned_dataframe["MonthlyCharges"] * cleaned_dataframe["tenure"]
    )

    cleaned_dataframe["SeniorCitizen"] = cleaned_dataframe["SeniorCitizen"].astype(int)
    cleaned_dataframe["tenure"] = cleaned_dataframe["tenure"].astype(int)
    cleaned_dataframe["MonthlyCharges"] = cleaned_dataframe["MonthlyCharges"].astype(float)
    cleaned_dataframe["TotalCharges"] = cleaned_dataframe["TotalCharges"].astype(float)

    categorical_columns = cleaned_dataframe.select_dtypes(include="object").columns
    cleaned_dataframe[categorical_columns] = cleaned_dataframe[categorical_columns].apply(
        lambda column: column.str.strip()
    )

    return cleaned_dataframe


def add_engineered_features(dataframe):
    """Create derived features useful for churn analysis."""
    engineered_dataframe = dataframe.copy()

    tenure_bins = [-1, 12, 24, 48, 60, 72]
    tenure_labels = [
        "0-12 Months",
        "13-24 Months",
        "25-48 Months",
        "49-60 Months",
        "61-72 Months",
    ]

    engineered_dataframe["tenure_group"] = pd.cut(
        engineered_dataframe["tenure"],
        bins=tenure_bins,
        labels=tenure_labels,
    )

    engineered_dataframe["avg_monthly_spend"] = np.where(
        engineered_dataframe["tenure"] > 0,
        engineered_dataframe["TotalCharges"] / engineered_dataframe["tenure"],
        engineered_dataframe["MonthlyCharges"],
    )

    return engineered_dataframe


def encode_dataset(dataframe):
    """Encode categorical columns for analytics and modeling readiness."""
    encoded_dataframe = dataframe.copy()

    binary_columns = ["Partner", "Dependents", "PhoneService", "PaperlessBilling", "Churn"]
    binary_mapping = {"Yes": 1, "No": 0}

    for column in binary_columns:
        encoded_dataframe[column] = encoded_dataframe[column].map(binary_mapping)

    encoded_dataframe["gender"] = encoded_dataframe["gender"].map({"Female": 0, "Male": 1})

    encoded_dataframe = pd.get_dummies(
        encoded_dataframe,
        columns=[
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaymentMethod",
            "tenure_group",
        ],
        drop_first=False,
        dtype=int,
    )

    return encoded_dataframe


def prepare_churn_data(file_path=RAW_DATA_PATH):
    """Run the full churn cleaning pipeline."""
    raw_dataframe = load_dataset(file_path)
    cleaned_dataframe = clean_dataset(raw_dataframe)
    enriched_dataframe = add_engineered_features(cleaned_dataframe)
    encoded_dataframe = encode_dataset(enriched_dataframe)
    return enriched_dataframe, encoded_dataframe


def save_cleaned_data(dataframe, output_path=OUTPUT_DATA_PATH):
    """Save the cleaned and encoded dataset to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)


def main():
    """Run the data-preparation pipeline and save the final dataset."""
    _, encoded_dataframe = prepare_churn_data()
    save_cleaned_data(encoded_dataframe)
    print(f"Cleaned dataset saved to: {OUTPUT_DATA_PATH}")


if __name__ == "__main__":
    main()
