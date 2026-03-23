# Week 3 Summary: NumPy and Pandas

## Overview

This week introduces two essential libraries for data analytics in Python:

- NumPy for fast numerical computing
- Pandas for working with structured and tabular data

These tools form the core of many data analysis, machine learning, and reporting workflows.

## NumPy Concepts

### Arrays

NumPy arrays are efficient data structures for storing numerical values. They are faster and more memory-efficient than standard Python lists for numerical tasks.

This week covered:

- one-dimensional arrays
- two-dimensional arrays
- element-wise operations

### Array Operations

NumPy supports vectorized operations, which means calculations can be applied to entire arrays at once.

Examples implemented:

- sum of array values
- mean of array values
- squaring each element
- scaling values by a constant

### Broadcasting

Broadcasting allows NumPy to perform arithmetic on arrays of different but compatible shapes without writing explicit loops.

In this week, broadcasting was demonstrated by adding a row vector to every row in a matrix.

## Pandas Concepts

### DataFrames

A Pandas DataFrame is a two-dimensional table with rows and columns. It is commonly used for dataset cleaning, transformation, aggregation, and reporting.

This week included:

- creating a sample DataFrame
- inspecting structured employee data

### Handling Missing Values

Missing values are common in real datasets. Pandas provides tools to detect and fill them.

This week used:

- median-based filling for missing salary values
- median-based filling for missing experience values

### GroupBy Operations

`groupby()` helps summarize data by categories.

This week included grouped analysis by department to calculate:

- average salary
- maximum experience
- employee count

### Basic Statistics

Pandas provides quick summary metrics for numeric columns using `.describe()`.

This helps analysts understand:

- count
- mean
- standard deviation
- minimum and maximum values

## What Was Implemented

### `numpy_practice.py`

- sample array creation
- element-wise array operations
- aggregation functions
- broadcasting example

### `pandas_analysis.py`

- sample DataFrame creation
- missing value handling
- grouped summaries
- descriptive statistics

## Coding Practices Followed

- clear function-based design
- reusable data-processing steps
- readable output for learning and demonstration
- clean structure suitable for GitHub projects
