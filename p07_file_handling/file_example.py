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

# Pathlib practice
from pathlib import Path


# file_path = Path("p07_file_handling/sample.txt") ; relative path
folder = Path("p07_file_handling")
file_path = folder / "sample.txt"

print(folder)
print(file_path)
print(file_path.exists())

print()

print(file_path)
print(type(file_path))
print(file_path.name)
print(file_path.parent)
print(file_path.exists())

# p07_file_handling/sample.txt   ← file_path
# <class 'pathlib.PosixPath'>    ← object type
# sample.txt                     ← file_path.name
# p07_file_handling              ← file_path.parent
# True                           ← file_path.exists()

# Using __file__ practice
print()
print(__file__)
print()

current_file = Path(__file__)

print(current_file)
print(current_file.name)
print(current_file.parent)

print()

# Absolute path
current_folder = Path(__file__).parent
sample_path = current_folder / "sample.txt"

print(sample_path)
print(sample_path.exists())
print()

with open(sample_path, "r") as file:
    content = file.read()

print(content)

# .is_file() ; .is_dir()
print(sample_path.exists())
print(sample_path.is_file())
print(sample_path.is_dir())
print()
print(current_folder.exists())
print(current_folder.is_file())
print(current_folder.is_dir())
print()

# Create a directory
output_folder = current_folder / "output"

# Use mkdir(exist_ok=True) to avoid an error if the directory already exists.
output_folder.mkdir(exist_ok=True) 

print(output_folder)
print(output_folder.exists())
print(output_folder.is_dir())

# Create nested directories
backup_folder = current_folder / "data" / "backup" / "2026"

# backup_folder.mkdir()  ;  It cannot be created because parent directory is not exist.

backup_folder.mkdir(parents=True, exist_ok=True)