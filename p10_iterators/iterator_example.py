numbers = [10, 20, 30]

# Create an iterator from a list.
number_iterator = iter(numbers)

# StopIteration occurs when the iterator is exhausted.
# print(next(number_iterator))
# print(next(number_iterator))
# print(next(number_iterator))
# print(next(number_iterator))

print(number_iterator)
print()

# An iterator is exhausted after one complete iteration.
for number in number_iterator:
    print(number)

print()

for number in number_iterator:
    print(number)

print()

# A list can be iterated over multiple times.
print(numbers)
print()

for number in numbers:
    print(number)

print()

for number in numbers:
    print(number)

print()

# Multiple independent iterators can be created from the same list.
iterator1 = iter(numbers)
iterator2 = iter(numbers)

print(next(iterator1))
print(next(iterator1))
print()
print(next(iterator2))
print("-----------------------")
print()

# Generator function
def generate_numbers():
    print("Before yield 1")
    yield 1

    print("Before yield 2")
    yield 2

    print("Before yield 3")
    yield 3

    print("Generator finished")


generated_numbers = generate_numbers()

print("Generator created")
print()

print(next(generated_numbers))
print()
print(next(generated_numbers))
print()
# Even after the third next() call, "Generator finished" is not printed,
# because the generator pauses at yield 3.
print(next(generated_numbers))
print()

# Iterate over a generator with a for loop
print("-----------------------")
print("Iterate over a generator with a for loop:")
print()


def generate_letters():
    yield "A"
    yield "B"
    yield "C"


letters = generate_letters()

for letter in letters:
    print(letter)

print()

# Nothing is printed because the generator is exhausted.
for letter in letters:
    print(letter)

# Generate values lazily
print("-----------------------")
print("Generate values lazily:")
print()


def generate_numbers():
    for number in range(5):
        print(f"Generating: {number}")
        yield number


numbers = generate_numbers()

print("Generator created")
print()

print(next(numbers))
print()
print(next(numbers))

# Compare memory usage
import sys


print("-----------------------")
print("Compare memory usage:")
print()

# List comprehension uses [].
number_list = [number for number in range(1_000_000)]

# Generator expression uses ().
number_generator = (number for number in range(1_000_000))

print(f"List: {sys.getsizeof(number_list)} bytes")
print(f"Generator: {sys.getsizeof(number_generator)} bytes")

# Compare list and generator behavior
print("-----------------------")
print("Compare list and generator behavior:")
print()

number_list = [10, 20, 30]
number_generator = (number for number in [10, 20, 30])

print(number_list[1])
print()
# A generator does not support indexing.
# print(number_generator[1])


# Generator Expression practice
print("-----------------------")
print("Generator Expression practice:")
print()

numbers = [1, 2, 3, 4, 5, 6]

squared_even_generator = (
    number ** 2 for number in numbers if number % 2 == 0
)

print(squared_even_generator)
print()

for number in squared_even_generator:
    print(number)
