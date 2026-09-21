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