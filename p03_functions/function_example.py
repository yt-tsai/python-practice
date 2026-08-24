# Function without a default argument

# def introduce(name, language):
#     return f"{name} is learning {language}."
# message = introduce("Peter", "Python")
# print(message)


# Function with a default argument


def introduce(name, language="Python"):
    return f"{name} is learning {language}."


message_1 = introduce("Peter")
message_2 = introduce("Marina", "Java")
print(message_1)
print(message_2)
line = "-------------------------------------------"
print(line)

# Positional arguments vs. Keyword arguments

message_positional = introduce("Marina", "Java")
message_keyword = introduce(language="Java", name="Marina")
print(message_positional)
print(message_keyword)


# Calculate Function


def calculate_total(price, quantity):
    # result = price * quantity
    # return result
    return price * quantity


total = calculate_total(120, 3)
print(line)
print(f"120 x 3 = {total}")

tax = total * 0.1
grand_total = total + tax
print(line)
print(f"Tax: {tax}")
print(f"Grand total: {grand_total}")

print(line)


def calculate_without_return(price, quantity):
    print(price * quantity)


# A function without a return statement returns None.
result_check = calculate_without_return(120, 3)
print(f"Returned value: {result_check}")
