# explore_datetime.py
# Objective: Work with Python's datetime module to display and calculate dates.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return for reuse in other functions


def calculate_future_date(current_date, days_to_add):
    """
    Calculates and prints the future date after adding a specified number of days.
    """
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")


if __name__ == "__main__":
    main()
