try:
    number1 = 10
    number2 = 0

    result = number1 / number2
    print(result)

# ZeroDivisionError: division by zero
except ZeroDivisionError as e:
    print(f"Error: {e}")

print("Program continues. v1")
print()

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid input. You need to enter an integer.")

except ZeroDivisionError as e:
    print(f"Cannot divide by zero: {e}")

else:
    print(f"100 / {number} = {result}")


# "finally" is executed regardless of whether an exception occurs.
finally:
    print("Calculation test-1 finished.")

print("Program continues. v2")
print()
print("---------------------------------------")

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

else:
    print(f"100 / {number} = {result}")

print("Calculation test-2 finished.")

print("Program continues. v3")
print()
print("---------------------------------------")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
    print(f"Error: {e}")

else:
    print(f"Your age is {age}.")

print("Calculation test-3 finished.")

print()
print("---------------------------------------")


# Function Practice
def calculate_average(total, count):
    if count == 0:
        raise ValueError("Count cannot be zero.")

    return total / count


try:
    # result = calculate_average(500, 5)
    result = calculate_average(500, 0)

except ValueError as e:
    print(f"Error: {e}")

else:
    print(result)

print("Calculation test-4 finished.")
