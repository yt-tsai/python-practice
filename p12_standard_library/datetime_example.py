# datetime basics
print("-- datetime basics --")

from datetime import datetime


now = datetime.now()

print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)