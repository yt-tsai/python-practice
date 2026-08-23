# Set
# A set uses curly braces like a dictionary,
# but it stores only unique elements.
line = "-------------------------"

languages = {
    "Java", "Python", "SQL", "Java", "Python"
}

# Duplicate elements are automatically removed.
print(languages)
print(len(languages))

print(line)
languages.add("JavaScript")
languages.add("Servlet")
languages.remove("SQL")

print("Java" in languages)
print("SQL" in languages)

print(line)
print(languages)
print(len(languages))

print(line)
languages.add("Java")
print(languages)
print(len(languages))

print(line)
for language in languages:
    print(language)

