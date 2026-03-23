# Week 2 Summary: Data Structures

## Overview

This week focuses on Python data structures and how they support common data-processing tasks such as filtering, transformation, and cleaning.

## Core Data Structures

### Lists

Lists are ordered and mutable collections. They are useful when storing sequences of values that may need to be updated, filtered, or transformed.

Examples used this week:

- storing numeric values for list operations
- storing simulated dataset records

### Tuples

Tuples are ordered and immutable collections. They are helpful when returning multiple related values from a function in a structured way.

In this week, the cleaning workflow returns multiple outputs together:

- cleaned records
- unique cities
- city counts

### Sets

Sets store unique values only. They are useful for removing duplicates and identifying distinct categories.

This week, sets were used to:

- collect unique city names
- support data-cleaning logic focused on uniqueness

### Dictionaries

Dictionaries store data as key-value pairs. They are widely used in analytics workflows because they model records and mappings clearly.

This week, dictionaries were used to:

- represent each dataset row as a record
- track records by unique id
- store counts by city

## Functions and Lambda

Functions help organize logic into reusable and readable units. Each script in Week 2 uses dedicated functions for transformation and validation tasks.

Lambda functions provide a concise way to define small anonymous functions. In `list_operations.py`, a lambda is used with `filter()` to keep numbers above a threshold.

## List Comprehension

List comprehension is a compact and readable way to create new lists from existing iterables.

This week, list comprehension was used for:

- selecting even numbers
- squaring numbers
- filtering valid records

## What Was Implemented

### `list_operations.py`

- list comprehension examples
- filtering operations
- sum of squares calculation
- reusable utility functions

### `data_cleaning.py`

- duplicate removal using dictionaries
- invalid record filtering
- unique value extraction using sets
- summary counts using dictionaries

## Coding Practices Followed

- small and focused functions
- meaningful variable names
- simple validation rules
- modular code ready for GitHub submission
