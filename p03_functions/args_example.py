# *args example
# *args collects multiple positional arguments into a tuple.


def calculate_total(*numbers):
    return sum(numbers)


total_1 = calculate_total(10, 20)
total_2 = calculate_total(10, 20, 30)
total_3 = calculate_total(10, 20, 30, 40)

print(total_1)
print(total_2)
print(total_3)
