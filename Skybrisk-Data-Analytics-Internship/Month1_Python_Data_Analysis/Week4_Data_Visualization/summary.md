# Week 4 Summary: Data Visualization

## Overview

This week focuses on presenting data visually using Matplotlib and Seaborn. Visualizations help analysts identify patterns, relationships, trends, and outliers more effectively than raw tables alone.

## Matplotlib

Matplotlib is a foundational Python library for creating static plots and charts. It gives precise control over figure size, labels, titles, axes, and file export.

This week, Matplotlib was used to:

- create plot figures
- set titles and axis labels
- control layout
- save plots as image files

## Seaborn

Seaborn is built on top of Matplotlib and provides a cleaner, higher-level interface for statistical visualizations. It simplifies styling and helps create more polished charts with less code.

This week, Seaborn was used to generate:

- a histogram for score distribution
- a scatter plot for relationship analysis
- a heatmap for correlations

## Visualizations Implemented

### Histogram

A histogram shows the distribution of a numeric variable by grouping values into bins.

Use in this week:

- understanding how exam scores are distributed

### Scatter Plot

A scatter plot helps analyze the relationship between two numeric variables.

Use in this week:

- comparing hours studied with exam scores
- adding attendance as a visual dimension using color

### Heatmap

A heatmap is useful for visualizing correlation strength between numeric variables.

Use in this week:

- understanding how study hours, exam scores, and attendance relate to one another

## What Was Implemented

### `visualization.py`

- created a sample dataset using Pandas
- generated a histogram
- generated a scatter plot
- generated a heatmap
- saved all plots in the `plots` folder

## Coding Practices Followed

- function-based plotting workflow
- reusable directory handling
- readable labels and titles
- clean structure ready for GitHub submission
