# Function review


def calculate_average(*scores):
    return sum(scores) / len(scores)


student_name = "Peter"

average = calculate_average(80, 90, 85)

print(f"Student: {student_name}")
print(f"Average: {average}")