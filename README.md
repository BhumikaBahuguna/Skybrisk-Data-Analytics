# Skybrisk Data Analytics Internship

This repository contains a completed structured data analytics internship project built in a phase-wise format. The work covers Python fundamentals, core data analysis libraries, visualization, and two end-to-end exploratory data analysis projects using real datasets.

## Project Status

The internship repository is complete up to:

- Month 1: Weekly Python and data analysis foundations
- Month 2: Applied EDA case studies

## Repository Structure

```text
Skybrisk-Data-Analytics/
|-- README.md
`-- Skybrisk-Data-Analytics-Internship/
    |-- requirements.txt
    |-- Month1_Python_Data_Analysis/
    |   |-- Week1_Python_Basics/
    |   |-- Week2_Data_Structures/
    |   |-- Week3_NumPy_Pandas/
    |   `-- Week4_Data_Visualization/
    |-- Task3_Customer_Churn_EDA/
    `-- Task4_Netflix_EDA/
```

## Month 1: Python Data Analysis Foundations

### Week 1: Python Basics

Implemented:

- temperature converter with input validation
- calculator using functions for arithmetic operations
- average temperature calculator from a list of values
- summary of core Python concepts

Key concepts:

- variables
- data types
- conditionals
- loops
- functions

### Week 2: Data Structures

Implemented:

- list operations with list comprehension and filtering
- simulated data cleaning using dictionaries and sets
- summary of Python data structures and lambda usage

Key concepts:

- lists
- tuples
- sets
- dictionaries
- list comprehension
- lambda functions

### Week 3: NumPy and Pandas

Implemented:

- NumPy array creation and operations
- broadcasting examples
- Pandas DataFrame creation and cleaning
- groupby analysis and descriptive statistics

Key concepts:

- arrays
- vectorized operations
- broadcasting
- dataframes
- missing value handling
- aggregation

### Week 4: Data Visualization

Implemented:

- histogram
- scatter plot
- correlation heatmap
- saved plot outputs in a dedicated `plots` folder

Libraries used:

- Matplotlib
- Seaborn

## Month 2: Applied EDA Projects

### Task 3: Customer Churn EDA

Dataset used:

- Telco Customer Churn dataset

Deliverables:

- notebook: `notebooks/churn_analysis.ipynb`
- script: `scripts/churn_cleaning.py`
- cleaned output: `data/cleaned_data.csv`
- business summary: `insights.md`

Work completed:

- dataset loading
- missing value handling
- data type conversion
- feature engineering for `tenure_group` and `avg_monthly_spend`
- categorical encoding
- churn-focused visual analysis

Visual analysis included:

- churn count plot
- contract vs churn
- heatmap
- boxplot

### Task 4: Netflix EDA

Dataset used:

- Netflix titles dataset

Deliverables:

- notebook: `notebooks/netflix_analysis.ipynb`
- saved charts in `visuals/`
- business interpretation in `insights.md`

Work completed:

- dataset cleaning
- `date_added` conversion
- feature engineering for content type, added year, genre, country, and release decade
- exploratory visual analysis
- simple trend prediction logic

Visual analysis included:

- content type pie chart
- yearly trend chart
- top genres chart
- country heatmap

## Tools and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Setup and Installation

From the project root:

```bash
pip install -r Skybrisk-Data-Analytics-Internship/requirements.txt
```

## How to Run

### Run Python Practice Files

Examples:

```bash
python Skybrisk-Data-Analytics-Internship/Month1_Python_Data_Analysis/Week1_Python_Basics/calculator.py
python Skybrisk-Data-Analytics-Internship/Month1_Python_Data_Analysis/Week3_NumPy_Pandas/pandas_analysis.py
python Skybrisk-Data-Analytics-Internship/Month1_Python_Data_Analysis/Week4_Data_Visualization/visualization.py
```

### Run Customer Churn Data Pipeline

```bash
python Skybrisk-Data-Analytics-Internship/Task3_Customer_Churn_EDA/scripts/churn_cleaning.py
```

### Open Notebooks

```bash
jupyter notebook
```

Then open:

- `Skybrisk-Data-Analytics-Internship/Task3_Customer_Churn_EDA/notebooks/churn_analysis.ipynb`
- `Skybrisk-Data-Analytics-Internship/Task4_Netflix_EDA/notebooks/netflix_analysis.ipynb`

## Highlights

- Structured week-wise learning progression
- Clean and reusable Python scripts
- Documented summaries for each foundational week
- Real-dataset EDA projects with notebooks and insights
- Saved visual outputs for both learning and presentation

## Future Improvements

- add a `.gitignore` for cache files and notebook artifacts
- remove generated `__pycache__` files before final publishing
- add screenshots of key plots to this README
- include a short portfolio summary for recruiters and mentors
