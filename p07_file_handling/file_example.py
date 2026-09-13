with open("p07_file_handling/sample.txt", "w") as file:
    file.write("Hello, Python!\n")

# Append the following text to the existing file:
# "I am learning File Handling.\n"

with open("p07_file_handling/sample.txt", "a") as file:
    file.write("I am learning File Handling.\n")

# "w" (write)
# Existing content: overwritten
# Write position: from the beginning
# If the file does not exist: create it

# "a" (append)
# Existing content: preserved
# Write position: at the end
# If the file does not exist: create it

with open("p07_file_handling/sample.txt", "r") as file:
    content = file.read()

print(content)


# file.writelines()
# readline()
languages = ["Python\n", "Java\n", "SQL\n"]

with open("p07_file_handling/languages.txt", "w") as file:
    file.writelines(languages)

with open("p07_file_handling/languages.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1.strip())
print(line2.strip())
print()


# readlines()
with open("p07_file_handling/languages.txt", "r") as file:
    lines = file.readlines()

print(lines)
print(type(lines))
print()

# read()      -->  str  -->  read the entire file
# readline()  -->  str  -->  read one line at a time
# readlines() -->  list -->  read all lines into a list


# Read the file line by line
with open("p07_file_handling/languages.txt", "r") as file:
    for line in file:
        print(line.strip())


# Exception handling practice
try:
    with open("p07_file_handling/not_found.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

finally:
    print("File operation finished.")