"""NumPy practice examples for array operations and broadcasting."""

import numpy as np


def create_sample_arrays():
    """Create sample NumPy arrays used throughout the examples."""
    one_dimensional = np.array([10, 20, 30, 40, 50])
    two_dimensional = np.array([[1, 2, 3], [4, 5, 6]])
    return one_dimensional, two_dimensional


def perform_array_operations(array):
    """Return common aggregate and element-wise operations."""
    return {
        "sum": np.sum(array),
        "mean": np.mean(array),
        "squared": array ** 2,
        "scaled_by_two": array * 2,
    }


def demonstrate_broadcasting(matrix):
    """Show NumPy broadcasting by adding a row vector to each row."""
    adjustment_vector = np.array([10, 20, 30])
    broadcasted_result = matrix + adjustment_vector
    return adjustment_vector, broadcasted_result


def main():
    """Run the NumPy practice workflow."""
    one_dimensional, two_dimensional = create_sample_arrays()
    array_results = perform_array_operations(one_dimensional)
    adjustment_vector, broadcasted_result = demonstrate_broadcasting(two_dimensional)

    print("One-dimensional array:")
    print(one_dimensional)

    print("\nTwo-dimensional array:")
    print(two_dimensional)

    print("\nArray operations:")
    for label, value in array_results.items():
        print(f"{label}: {value}")

    print("\nBroadcasting vector:")
    print(adjustment_vector)

    print("\nBroadcasting result:")
    print(broadcasted_result)


if __name__ == "__main__":
    main()
