task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

message = ""

match priority:
    case "high":
        if time_bound == "yes":
            message = f"Reminder: {task} is a high priority task that requires immediate attention today!"
        else:
            message = f"Reminder: {task} is a high priority task. Consider completing it when you have free time."
    case "medium":
        if time_bound == "yes":
            message = f"Reminder: {task} is a medium priority task with time sensitivity. Plan accordingly."
        else:
            message = f"Reminder: {task} is a medium priority task. You have some flexibility to finish this."
    case "low":
        if time_bound == "yes":
            message = f"Reminder: {task} is a low priority task, but there is a deadline to keep in mind."
        else:
            message = f"Reminder: {task} is a low priority task. No rush, handle it when you can."
    case _:
        message = "Invalid priority input. Please enter 'high', 'medium', or 'low'."

print("\nReminder:")
print(message)