class Student:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def introduce(self):
        print(f"My name is {self.name} and I am learning {self.language}.")


# Child class can inherit the parent class without additional parameters.
# class AdvancedStudent(Student):
#     pass

# Child class inherits from the parent class and adds a parameter.
class AdvancedStudent(Student):

    def __init__(self, name, language, experience=3):
        super().__init__(name, language)
        self.experience = experience

    def introduce(self):
        print(
            f"My name is {self.name}, "
            f"I am learning {self.language}, "
            f"and I have {self.experience} years of experience."
        )


student1 = Student("Peter", "Python")
student1.introduce()

print()

advanced_student2 = AdvancedStudent("Peter-advanced", "Python", 8)
print(advanced_student2.name)
print(advanced_student2.language)
print(advanced_student2.experience)
advanced_student2.introduce()

print()

students = [student1, advanced_student2]

for student in students:
    student.introduce()


# Duck Typing example:
class Teacher:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am a teacher. My name is {self.name}.")


teacher1 = Teacher("John")

# Duck typing: different classes can use the same method interface.
people = [student1, advanced_student2, teacher1]

print()

for person in people:
    person.introduce()