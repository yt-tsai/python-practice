# Tuple 
# A tuple is immutable, while a list is mutable.

languages = ("Java", "Python", "SQL")
line = "-------------------------------"
print(line)
print(languages)
print(languages[0])
print(len(languages))

print(line)
for language in languages:
    print(language)

print(line)

# A tuple cannot be modified after it is created.
# languages[1] = "JavaScript"  # TypeError: tuples are immutable.
