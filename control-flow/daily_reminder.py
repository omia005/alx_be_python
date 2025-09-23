task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
   case "high":
     reminder = f"Reminder: '{task}' is a high priority task."
   case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
   case "low":
        reminder = f"Reminder: '{task}' is a low priority task."

if time_bound == "yes":
     print(" This task requires immediate attention today!")
else:
    print(" Consider completing it when you have free time.")
  
     
