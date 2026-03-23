"""Average temperature calculator."""


def calculate_average(temperatures):
    """Return the average temperature from a list of numeric values."""
    if not temperatures:
        raise ValueError("Temperature list cannot be empty.")

    return sum(temperatures) / len(temperatures)


def parse_temperature_list(raw_values):
    """Parse a comma-separated string into a list of temperatures."""
    values = [item.strip() for item in raw_values.split(",") if item.strip()]

    if not values:
        raise ValueError("Please provide at least one temperature value.")

    try:
        return [float(value) for value in values]
    except ValueError as error:
        raise ValueError("All temperature values must be valid numbers.") from error


def main():
    """Run the average temperature calculator."""
    print("Average Temperature Calculator")
    print("Enter temperatures separated by commas.")

    user_input = input("Temperatures: ").strip()

    try:
        temperatures = parse_temperature_list(user_input)
        average_temperature = calculate_average(temperatures)
        print(f"Average temperature: {average_temperature:.2f}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
