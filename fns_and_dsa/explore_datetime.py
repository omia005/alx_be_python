import datetime, timedelta from datetime

def display_current_datetime():
  current_date = datetime.now()
  print("Today's date and time:", current_date.strftime("%A, %B %d, %Y %I:%M:%S %p"))

days_to_add = input("enter a number of days (as an integer):")

def calculate_future_date(days_to_add):
  future_date = display_current_datetime() + timedelta(days= days_to_add)
  print(" Future days from now:", future_date)
