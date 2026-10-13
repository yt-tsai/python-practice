# datetime basics
print("-- datetime basics --")

from datetime import datetime, timedelta


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
print()


# Timedelta basics
print("-- Timedelta basics --")

today = datetime(2026, 10, 12)

next_week = today + timedelta(days=7)
last_week = today - timedelta(days=7)

created_date = datetime(2026, 9, 24)
issue_age = today - created_date

print(f"Next week: {next_week}")
print(f"Last week: {last_week}")
print(f"Issue age: {issue_age.days} days")
print()


# Timedelta total seconds
print("-- Timedelta total seconds --")

start_time = datetime(2026, 10, 13, 15, 0)
end_time = datetime(2026, 10, 15, 14, 30)

duration = end_time - start_time

total_hours = duration.total_seconds() / (60 * 60)

print(f"Duration: {duration}")
print(f"Total hours: {total_hours}")
