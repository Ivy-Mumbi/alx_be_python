# daily_reminder.py
# Objective: Use conditionals, match case, and loops to remind the user about a single, priority task based on time sensitivity.

while True:
    # Prompt for user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Use match case to process based on priority
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please use 'high', 'medium', or 'low'.\n")
            continue  # Repeat loop if invalid input is given

    # Add message based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        if priority == "low":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += " that you can schedule for later today."

    # Display the customized reminder
    print("\n" + reminder + "\n")

    # Ask if the user wants to enter another task
    repeat = input("Would you like to enter another task? (yes/no): ").lower()
    if repeat != "yes":
        print("All reminders set. Have a productive day!")
        break

