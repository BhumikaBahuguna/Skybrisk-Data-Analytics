"""Examples of common list operations used in data preparation."""


def filter_even_numbers(numbers):
    """Return only even numbers from the input list."""
    return [number for number in numbers if number % 2 == 0]


def square_numbers(numbers):
    """Return a list containing the square of each input number."""
    return [number ** 2 for number in numbers]


def sum_of_squares(numbers):
    """Return the sum of squares for the input list."""
    return sum(square_numbers(numbers))


def filter_by_threshold(numbers, threshold):
    """Filter numbers greater than or equal to the provided threshold."""
    return list(filter(lambda number: number >= threshold, numbers))


def main():
    """Run a simple demonstration of list operations."""
    sample_numbers = [2, 5, 8, 11, 14, 17, 20]

    even_numbers = filter_even_numbers(sample_numbers)
    squared_numbers = square_numbers(sample_numbers)
    threshold_numbers = filter_by_threshold(sample_numbers, 10)
    total_sum_of_squares = sum_of_squares(sample_numbers)

    print("Original numbers:", sample_numbers)
    print("Even numbers:", even_numbers)
    print("Squared numbers:", squared_numbers)
    print("Numbers greater than or equal to 10:", threshold_numbers)
    print("Sum of squares:", total_sum_of_squares)


if __name__ == "__main__":
    main()
