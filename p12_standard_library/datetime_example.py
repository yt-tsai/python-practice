# datetime basics
print("-- datetime basics --")

from datetime import datetime


now = datetime.now()

print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print()


# Date formatting
print("-- Date formatting --")

formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M")
formatted_datetime = now.strftime("%Y-%m-%d %H:%M")

print(formatted_date)
print(formatted_time)
print(formatted_datetime)
print()


# Date parsing
print("-- Date parsing --")

date_text = "2026-10-11"

parsed_date = datetime.strptime(date_text, "%Y-%m-%d")

print(parsed_date)
print(parsed_date.year)
print(parsed_date.month)
print(parsed_date.day)
print(type(parsed_date))