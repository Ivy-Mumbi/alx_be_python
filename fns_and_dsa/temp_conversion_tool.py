# temp_conversion_tool.py
# Objective: Demonstrate variable scope using global conversion factors for temperature conversion.

# --- Definition of Global Conversion Factors ---
# These constants define how temperatures are converted between Fahrenheit and Celsius.
# FAHRENHEIT_TO_CELSIUS_FACTOR: Multiply the Fahrenheit difference (F - 32) by this factor to get Celsius.
# CELSIUS_TO_FAHRENHEIT_FACTOR: Multiply the Celsius value by this factor and add 32 to get Fahrenheit.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# --- Conversion Functions ---
def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global conversion factor.
    Formula: (F - 32) * 5/9
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global conversion factor.
    Formula: (C * 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# --- Main Function ---
def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # Validate numeric input

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


# --- Script Entry Point ---
if __name__ == "__main__":
    main()

