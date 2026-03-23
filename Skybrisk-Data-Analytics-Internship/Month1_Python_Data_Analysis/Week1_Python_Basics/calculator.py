"""Basic calculator implementation using functions."""


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference of two numbers."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Return the quotient of two numbers."""
    if second_number == 0:
        raise ValueError("Division by zero is not allowed.")
    return first_number / second_number


def calculate(first_number, second_number, operator):
    """Perform a calculation for the supported arithmetic operators."""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if operator not in operations:
        raise ValueError("Operator must be one of: +, -, *, /")

    return operations[operator](first_number, second_number)


def parse_number(value):
    """Convert a user input string into a floating-point number."""
    try:
        return float(value)
    except ValueError as error:
        raise ValueError("Input must be a valid number.") from error


def main():
    """Run the interactive calculator."""
    print("Basic Calculator")

    try:
        first_number = parse_number(input("First number: ").strip())
        operator = input("Operator (+, -, *, /): ").strip()
        second_number = parse_number(input("Second number: ").strip())

        result = calculate(first_number, second_number, operator)
        print(f"Result: {result:.2f}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
