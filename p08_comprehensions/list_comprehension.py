numbers = [1, 2, 3, 4, 5]

squares = []

# Traditional for loop
for number in numbers:
    squares.append(number ** 2)

print(squares)

# List comprehension
squares_comprehension = [number ** 2 for number in numbers]

print(squares_comprehension)

# Squares of even numbers only
even_squares = [number ** 2 for number in numbers if number % 2 == 0]

print(even_squares)

# Words longer than 4 characters
words = ["Java", "Python", "SQL", "Spring"]

long_words = [word for word in words if len(word) > 4]

print(long_words)

# Convert words to uppercase
languages = ["python", "java", "sql", "javascript"]

upper_languages = [language.upper() for language in languages]

print(upper_languages)
print()

long_upper_languages = [language.upper() for language in languages if len(language) > 4]

print(long_upper_languages)
print()

# List comprehension with if...else
numbers = [1, 2, 3, 4, 5]

labels = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]

print(numbers)
print(labels)
print()

# Conditional expression practice
scores = [85, 42, 73, 58, 90]

results = [
    "Pass" if score >= 60 else "Fail"
    for score in scores
]

print(scores)
print(results)
