# Traditional function
def square(number):
    return number ** 2


print(square(5))
print()

# Lambda function
square_lambda = lambda number: number ** 2

print(square_lambda(6))
print()

# Lambda with two parameters
add_lambda = lambda parameter1, parameter2: parameter1 + parameter2

print(add_lambda(3, 5))
print()

# Sort with lambda
students = [
    ("Peter", 85),
    ("Amy", 92),
    ("John", 78),
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)
print()

# Traditional sort code
# def get_score(student):
#     return student[1]


# sorted_students = sorted(
#     students,
#     key=get_score
# )


# Sort words by length
languages = ["Python", "Java", "SQL", "JavaScript"]

sorted_languages = sorted(
    languages,
    # key=lambda language: len(language)
    key=len
)

print(sorted_languages)
print()

# Sort students by score in descending order
students_by_score_desc = sorted(
    students,
    key=lambda student: student[1],
    reverse=True,
)

print(students_by_score_desc)
print()

# Lambda with map()
numbers = [1, 2, 3, 4, 5]

# doubled_numbers = map(
#     lambda number: number * 2,
#     numbers
# )

# A map object is an iterator, so the second iteration will be empty.
# print(list(doubled_numbers))
# print()
# print(list(doubled_numbers))

doubled_numbers = list(
    map(
        lambda number: number * 2,
        numbers
    )
)

# A list can be reused after converting the map object.
print(doubled_numbers)
print()
print(doubled_numbers)
print()

# Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(
        lambda number: number % 2 == 0,
        numbers
    )
)

print(even_numbers)
print()

# Filter words by length
languages = ["Python", "Java", "SQL", "JavaScript", "C"]

long_languages = list(
    filter(
        lambda language: len(language) > 4,
        languages
    )
)

print(long_languages)
print()

# Combine filter() and map()
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(
        lambda number: number % 2 == 0,
        numbers
    )
)

squared_even_numbers = list(
    map(
        lambda number: number ** 2,
        even_numbers
    )
)

print(squared_even_numbers)
print()

# Combine filter() and map() in one expression
numbers = [1, 2, 3, 4, 5, 6]

squared_even_numbers = list(
    map(
        lambda number: number ** 2,
        filter(
            lambda number: number % 2 == 0,
            numbers
        )
    )
)

print(squared_even_numbers)
print()

# Find the student with the highest score
students = [
    ("Peter", 85),
    ("Marina", 92),
    ("Mika", 78),
]

highest_score_student = max(
    students,
    key=lambda student: student[1]
)

print(highest_score_student)
print()

# Find the student with the lowest score
lowest_score_student = min(
    students,
    key=lambda student: student[1]
)

print(lowest_score_student)
print()

# Find the student with the longest name
longest_name_student = max(
    students,
    key=lambda student: len(student[0])
)

print(longest_name_student)