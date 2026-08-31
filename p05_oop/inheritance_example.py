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


advanced_student1 = AdvancedStudent("Peter", "Python")
advanced_student1.introduce()

print()

advanced_student2 = AdvancedStudent("Peter", "Python", 5)
print(advanced_student2.name)
print(advanced_student2.language)
print(advanced_student2.experience)
advanced_student2.introduce()