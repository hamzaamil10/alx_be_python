task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nNote: '{task}' is a high priority task. Try to address it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"\nNote: '{task}' is a medium priority task. Plan to work on it this week.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task that still needs to be done today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"\nWarning: '{task}' has an unrecognized priority level.")
