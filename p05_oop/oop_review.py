class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            raise ValueError("Name cannot be empty.")
        self._name = new_name

    def introduce(self):
        print(f"My name is {self.name} and my salary is {self.salary}.")


# Java                         Python

# private name          ≈      _name
# getName()             ≈      @property name
# setName(...)          ≈      @name.setter

# employee.getName()           employee.name
# employee.setName("Peter")    employee.name = "Peter"


employee1 = Employee("Peter", 878787)

print(employee1.name)
print(employee1.salary)
employee1.introduce()

print()

try:
    employee2 = Employee("", 444444)
except ValueError as e:
    print(e)

line = "----------------------------------"
print(line)


class Engineer(Employee):
    # Inheritance
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    # Override
    def introduce(self):
        print(
            f"My name is {self.name}, "
            f"my salary is {self.salary}, "
            f"and I use {self.language}."
        )


engineer1 = Engineer("Marina", 999999, "Python")
print(engineer1.name)
print(engineer1.salary)
print(engineer1.language)
engineer1.introduce()

print(line)

# Polymorphism
employees = [employee1, engineer1]

for employee in employees:
    employee.introduce()

print(line)


# Duck Typing review
class Manager:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am a manager. My name is {self.name}.")


manager1 = Manager("John")

people = [employee1, engineer1, manager1]

for person in people:
    person.introduce()