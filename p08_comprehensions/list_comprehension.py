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
