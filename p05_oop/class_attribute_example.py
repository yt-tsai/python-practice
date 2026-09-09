class Student:
    # Class attribute
    school = "Python Academy"  # Shared by all instances

    def __init__(self, name):
        # Instance attribute
        self.name = name


student1 = Student("Peter")
student2 = Student("Marina")

print()
print(student1.name)
print(student1.school)
print()
print(student2.name)
print(student2.school)
print()
print(Student.school)
print()

student1.school = "Java Academy"
print(student1.school)
print(student2.school)
print(Student.school)

print()
Student.school = "AI Academy"
print(student1.school)
print(student2.school)
print(Student.school)