"""Temperature conversion utilities.

This module provides reusable functions to convert temperatures
between Celsius and Fahrenheit, along with a small command-line
interface for interactive use.
"""


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def parse_temperature(value):
    """Safely parse a numeric temperature value from user input."""
    try:
        return float(value)
    except ValueError as error:
        raise ValueError("Temperature must be a valid number.") from error


def convert_temperature(value, unit):
    """Convert temperature based on the provided source unit."""
    normalized_unit = unit.strip().upper()

    if normalized_unit == "C":
        converted_value = celsius_to_fahrenheit(value)
        return converted_value, "F"

    if normalized_unit == "F":
        converted_value = fahrenheit_to_celsius(value)
        return converted_value, "C"

    raise ValueError("Unit must be 'C' for Celsius or 'F' for Fahrenheit.")


def main():
    """Run the interactive temperature converter."""
    print("Temperature Converter")
    print("Enter a temperature and its unit to convert between C and F.")

    user_value = input("Temperature value: ").strip()
    user_unit = input("Current unit (C/F): ").strip()

    try:
        temperature = parse_temperature(user_value)
        converted_value, target_unit = convert_temperature(temperature, user_unit)
        print(f"Converted temperature: {converted_value:.2f} {target_unit}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
