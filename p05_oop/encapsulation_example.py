class Student:
    def __init__(self, name):
        # condition 1 -> ._name
        self._name = name

        # condition 2 -> .__name
        self.__name = name

    def introduce(self):
        # condition 1
        # print(f"My name is {self._name}.")

        # condition 2
        print(f"My name is {self.__name}.")


student1 = Student("Peter")
student1.introduce()

# Condition1
# Java              v.s.            Python
# ────────────────────────────────────────
# private String name               self._name
# Language-enforced restriction     Naming Convention
# Cannot be accessed externally     Can be accessed externally
# Emphasizes access control         Emphasizes developer convention
# print(student1._name)

# Condition2
# Python          description
# ────────────────────────────────────────────
# self.name       Public
# self._name      Internal-use convention
# self.__name     Name mangling
# print(student1.__name)

print(student1.__dict__)