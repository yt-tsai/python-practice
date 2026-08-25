# 1) Local variable


def show_language():
    language = "Python"  # Local variable
    print(language)


print()
print("1) Local variable: ")
show_language()

# A local variable cannot be accessed outside the function.
# print(language)


# 2) Global variable

language_2 = "Java"  # Global variable


def show_language_2():
    print(language_2)


print()
print("2) Global variable: ")
show_language_2()
print(language_2)

# 3) Global vs. local variable

language_3 = "Servlet"  # Global variable


def change_language():
    language_3 = "SQL"  # Local variable
    print(f"Inside: {language_3}")


print()
print("3) Global vs. local variable: ")
change_language()
print(f"Outside: {language_3}")

# 4) Modify global variable

language_4 = "Python"


def change_language_2():
    global language_4
    language_4 = "Java"


print()
print("4) Modify global variable: ")
print(f"Before: {language_4}")
change_language_2()
print(f"After: {language_4}")

# 5) Using return instead of global


def change_language_3(current_language, new_language):
    current_language = new_language  # Local variable
    return current_language


language_5 = "Python"  # Global variable

print()
print("5) Using return instead of global: ")
print(f"Before: {language_5}")

language_5 = change_language_3(language_5, "Java")  # Update the variable using the returned value.
print(f"After: {language_5}")
