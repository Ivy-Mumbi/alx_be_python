# daily_reminder.py
# Objective: Provide a customized reminder for a single priority task using conditionals, match case, and loops.

# Prompt for user input
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Process the task using match case
match priority:
    case "high":
        message = f"Reminder: Your high-priority task is '{task}'."
    case "medium":
        message = f"Reminder: Your medium-priority task is '{task}'."
    case "low":
        message = f"Reminder: Your low-priority task is '{task}'."
    case _:
        message = f"Reminder: Your task '{task}' has an unspecified priority."

# Adjust the reminder if the task is time-bound
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Display the customized reminder
print("\n" + message)
