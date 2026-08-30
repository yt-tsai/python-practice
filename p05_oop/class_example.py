class Student:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def introduce(self):
        print(f"My name is {self.name} and I am learning {self.language}.")

    def change_language(self, new_language):
        self.language = new_language


student_1 = Student("Peter", "Python")
student_2 = Student("Marina", "Java")

line = "--------------------------"
print(line)
print("STUDENT 1")
print(f"name: {student_1.name}")
print(f"lang: {student_1.language}")
student_1.introduce()

print(line)
print("STUDENT 2")
print(f"name: {student_2.name}")
print(f"lang: {student_2.language}")
student_2.introduce()

print(line)
print("STUDENT 1 AFTER LANGUAGE CHANGE")
student_1.change_language("Servlet")
student_1.introduce()
