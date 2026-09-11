class Student:
    def __init__(self, name):
        self.name = name  # Use the property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            raise ValueError("Name cannot be empty.")

        self._name = new_name


student = Student("Peter")

print(student.name)  # Getter

student.name = "Marina"  # Setter

print(student.name)  # Getter

# print()
# student.name = ""
# print(student.name)

try:
    student.name = ""
except ValueError as e:
    print(e)

print()
print(student.name)

try:
    student = Student("")
except ValueError as e:
    print(e)

print(student.name)
