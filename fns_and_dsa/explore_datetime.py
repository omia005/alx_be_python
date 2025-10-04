import datetime, timedelta from datetime

def display_current_datetime():
  current_date = datetime.now()
  formatted = now.strftime("%Y-%m-%d %H:%M:%S")
  print("Current date and time:", formatted)

days_to_add = input("Enter the number of days to add to the current date:")

def calculate_future_date(days_to_add):
  future_date = display_current_datetime() + timedelta(days= days_to_add)
  print(" Future days from now:", future_date)
