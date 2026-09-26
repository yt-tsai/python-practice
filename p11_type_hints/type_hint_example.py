# Traditional function method
def add(a, b):
    return a + b


result = add(10, 20)
print(result)
print()

# JAVA vs PYTHON
# Java                    Python

# int a                    a: int
# int b                    b: int
# int add(...)             (...) -> int

# Type Hint method
def add(a: int, b: int) -> int:
    return a + b


result = add(10, 20)
print(result)
print()

# Type hints are not enforced at runtime.
result_string = add("Hello", "Peter")
print(result_string)
print()

# Variable type hints
age: int = 42
name: str = "Peter"
weight: float = 65.8
is_engineer: bool = True

print(age)
print(name)
print(weight)
print(is_engineer)
print()

# Collection type hints
languages: list[str] = ["Java", "Python", "SQL"]
scores: dict[str, int] = {"Peter": 88, "Marina": 72, "Mika": 66}
profile: tuple[str, int] = ("Peter", 42)

print(languages)
print(scores)
print(profile)
print()

# Function + Collection Type Hint
def get_average(scores: list[float]) -> float:
    return sum(scores) / len(scores)


scores = [88.0, 77.0, 55.0]

scores_average = get_average(scores)
print(scores_average)
print()


# Union type hint
def find_language(language_id: int) -> str | None:
    if language_id == 1:
        return "Python"
    if language_id == 2:
        return "Java"
    return None

print("-- Union type hint --")
print(find_language(1))
print(find_language(2))
print(find_language(99))


# Union type with multiple possible types
def format_id(user_id: int | str) -> str:
    return "ID: " + str(user_id)


print("-- Union type --")
print(format_id(100))
print(format_id("A001"))
