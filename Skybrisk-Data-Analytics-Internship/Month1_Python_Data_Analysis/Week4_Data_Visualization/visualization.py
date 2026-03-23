"""Create and save basic data visualizations using Matplotlib and Seaborn."""

from pathlib import Path

import matplotlib
# Use a non-interactive backend so plots can be saved in headless environments.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


PLOTS_DIR = Path(__file__).resolve().parent / "plots"


def create_sample_dataframe():
    """Create a small sample dataset for plotting."""
    return pd.DataFrame(
        {
            "hours_studied": [2, 3, 4, 5, 6, 7, 8, 9],
            "exam_score": [55, 60, 64, 70, 76, 82, 88, 93],
            "attendance_percent": [65, 70, 72, 78, 82, 88, 91, 95],
        }
    )


def ensure_plots_directory():
    """Create the plots directory if it does not exist."""
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)


def save_histogram(dataframe):
    """Generate and save a histogram."""
    plt.figure(figsize=(8, 5))
    sns.histplot(data=dataframe, x="exam_score", bins=6, kde=True, color="steelblue")
    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "histogram_exam_scores.png")
    plt.close()


def save_scatter_plot(dataframe):
    """Generate and save a scatter plot."""
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=dataframe,
        x="hours_studied",
        y="exam_score",
        hue="attendance_percent",
        palette="viridis",
        s=100,
    )
    plt.title("Hours Studied vs Exam Score")
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Score")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "scatter_hours_vs_scores.png")
    plt.close()


def save_heatmap(dataframe):
    """Generate and save a correlation heatmap."""
    plt.figure(figsize=(7, 5))
    correlation_matrix = dataframe.corr(numeric_only=True)
    sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "heatmap_correlations.png")
    plt.close()


def main():
    """Create all required visualizations."""
    sns.set_theme(style="whitegrid")
    ensure_plots_directory()
    sample_dataframe = create_sample_dataframe()

    save_histogram(sample_dataframe)
    save_scatter_plot(sample_dataframe)
    save_heatmap(sample_dataframe)

    print(f"Plots saved to: {PLOTS_DIR}")


if __name__ == "__main__":
    main()
