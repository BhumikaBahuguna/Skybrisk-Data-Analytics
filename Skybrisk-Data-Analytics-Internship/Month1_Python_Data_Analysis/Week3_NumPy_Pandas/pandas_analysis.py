"""Pandas practice for creating, cleaning, and analyzing tabular data."""

import pandas as pd


def create_sample_dataframe():
    """Create a small sample dataset with intentional missing values."""
    return pd.DataFrame(
        {
            "department": ["Sales", "Sales", "HR", "HR", "IT", "IT"],
            "employee": ["Anaya", "Rohan", "Mira", "Kabir", "Ishaan", "Sara"],
            "salary": [55000, 60000, 50000, None, 70000, 72000],
            "experience_years": [2, 4, 3, 5, None, 6],
        }
    )


def clean_missing_values(dataframe):
    """Fill missing numeric values using median imputation."""
    cleaned_dataframe = dataframe.copy()
    cleaned_dataframe["salary"] = cleaned_dataframe["salary"].fillna(
        cleaned_dataframe["salary"].median()
    )
    cleaned_dataframe["experience_years"] = cleaned_dataframe["experience_years"].fillna(
        cleaned_dataframe["experience_years"].median()
    )
    return cleaned_dataframe


def generate_department_summary(dataframe):
    """Compute grouped statistics by department."""
    return dataframe.groupby("department").agg(
        average_salary=("salary", "mean"),
        max_experience=("experience_years", "max"),
        employee_count=("employee", "count"),
    )


def generate_basic_statistics(dataframe):
    """Return basic statistics for numeric columns."""
    return dataframe[["salary", "experience_years"]].describe()


def main():
    """Run the Pandas analysis workflow."""
    employee_dataframe = create_sample_dataframe()
    cleaned_dataframe = clean_missing_values(employee_dataframe)
    department_summary = generate_department_summary(cleaned_dataframe)
    statistics_summary = generate_basic_statistics(cleaned_dataframe)

    print("Original DataFrame:")
    print(employee_dataframe)

    print("\nCleaned DataFrame:")
    print(cleaned_dataframe)

    print("\nDepartment Summary:")
    print(department_summary)

    print("\nBasic Statistics:")
    print(statistics_summary)


if __name__ == "__main__":
    main()
