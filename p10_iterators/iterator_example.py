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

