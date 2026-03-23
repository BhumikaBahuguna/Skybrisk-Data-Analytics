# Week 1 Summary: Python Basics

## Overview

This week focuses on the building blocks of Python programming. The exercises were designed to reinforce core syntax, structured problem solving, and function-based coding practices.

## Key Concepts Covered

### Variables

Variables are used to store values that can be reused throughout a program. They help make code readable and maintainable by giving meaningful names to data.

Examples used in this week:

- `temperature`
- `converted_value`
- `first_number`
- `average_temperature`

### Data Types

Python supports multiple built-in data types. The Week 1 exercises mainly used:

- `str` for user input and operators
- `float` for numeric calculations
- `list` for storing temperature values
- `tuple` style return values when returning multiple results from a function

### Conditionals

Conditionals allow programs to make decisions based on rules.

Examples from this week:

- Checking whether the temperature unit is `C` or `F`
- Validating whether the selected calculator operator is supported
- Preventing division by zero
- Ensuring a temperature list is not empty

### Loops

Loops are used to repeat operations. In this week, looping appears indirectly through list processing and comprehensions used while parsing user input into multiple temperature values.

## What Was Implemented

### `temperature_converter.py`

- Converts Celsius to Fahrenheit
- Converts Fahrenheit to Celsius
- Validates numeric input
- Handles invalid units cleanly

### `calculator.py`

- Supports addition, subtraction, multiplication, and division
- Uses separate functions for each arithmetic operation
- Includes operator validation
- Prevents division by zero

### `avg_temperature.py`

- Accepts a list of temperature values
- Parses comma-separated input
- Computes the average using a reusable function
- Handles empty or invalid input safely

## Coding Practices Followed

- Small, focused functions
- Clear function names
- Helpful docstrings
- Basic input validation
- Readable program structure suitable for GitHub submission
