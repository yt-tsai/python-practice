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

# Positional arguments vs. keyword arguments

message_positional = introduce("Marina", "Java")
message_keyword = introduce(language="Java", name="Marina")
print(message_positional)
print(message_keyword)


