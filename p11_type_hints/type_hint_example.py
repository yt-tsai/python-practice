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
print()


# Class type hint
print("-- Class type hint --")


class User:
    def __init__(self, name: str):
        self.name = name


def show_user(user: User) -> None:
    print(f"User: {user.name}")


user = User("Peter")
show_user(user)
print()


# Callable type hint
print("-- Callable type hint --")
from collections.abc import Callable


def double(number: int) -> int:
    return number * 2


print(double(40))
print()


def apply_operation(
    number: int,
    operation: Callable[[int], int]
) -> int:
    return operation(number)


print(apply_operation(40, double))
print()


# Literal type hint
print("-- Literal type hint --")
from typing import Literal


def show_priority(priority: Literal["H", "M", "L"]) -> None:
    print(f"Priority: {priority}")


show_priority("H")
show_priority("M")
show_priority("L")
print()


# TypedDict type hint
print("-- TypedDict type hint --")
from typing import TypedDict


class IssueInfo(TypedDict):
    title: str
    priority: Literal["H", "M", "L"]
    progress: int


issue: IssueInfo = {
    "title": "Login error",
    "priority": "H",
    "progress": 50
}

print(issue)
print(issue["title"])
print(issue["priority"])
print(issue["progress"])
print()


# Type alias
print("-- Type alias --")

IssuePriority = Literal["H", "M", "L"]


def display_issue_priority(priority: IssuePriority) -> None:
    print(f"Issue priority: {priority}")


display_issue_priority("H")
display_issue_priority("M")
display_issue_priority("L")
print()


# Optional type hint
print("-- Optional type hint --")
from typing import Optional


def find_framework(framework_id: int) -> Optional[str]:
    if framework_id == 1:
        return "Spring Boot"
    if framework_id == 2:
        return "Django"
    return None


print(find_framework(1))
print(find_framework(2))
print(find_framework(99))
print()


# Any type hint
print("-- Any type hint --")

from typing import Any


def show_value(value: Any) -> None:
    print(f"Value: {value}")


show_value(100)
show_value("Python")
show_value(3.14)
show_value([1, 2, 3])
print()


# TypeVar type hint
print("-- TypeVar type hint --")

from typing import TypeVar


T = TypeVar("T")


def get_first(items: list[T]) -> T:
    return items[0]


print(get_first([10, 20, 30]))
print(get_first(["Python", "Java", "SQL"]))
print()


# Generic class
print("-- Generic class --")

from typing import Generic


class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value


number_container = Container[int](100)
text_container = Container[str]("Python")

print(number_container.get_value())
print(text_container.get_value())


# Protocol type hint
print("-- Protocol type hint --")

from typing import Protocol


class Printable(Protocol):
    def print_info(self) -> str:
        ...


class User:
    def __init__(self, name: str):
        self.name = name

    def print_info(self) -> str:
        return f"User: {self.name}"


def show_info(user: Printable) -> None:
    print(user.print_info())


user = User("Peter")
show_info(user)
print()


# Final type hint
print("-- Final type hint --")

from typing import Final

MAX_RETRIES: Final[int] = 3
APP_NAME: Final[str] = "Technical Issue Manager"

print(MAX_RETRIES)
print(APP_NAME)
print()


# ClassVar type hint
print("-- ClassVar type hint --")

from typing import ClassVar


class Employee:
    company: ClassVar[str] = "Tech Corp"

    def __init__(self, name: str):
        self.name = name


employee1 = Employee("Peter")
employee2 = Employee("Marina")

print(Employee.company)
print(employee1.name)
print(employee2.name)
print()


# cast type hint
print("-- cast type hint --")

from typing import Any, cast

value: Any = "Python"

text = cast(str, value)

print(text.upper())
print()


# overload type hint
print("-- overload type hint --")

from typing import overload


@overload
def format_value(value: int) -> str:
    ...


@overload
def format_value(value: float) -> str:
    ...


def format_value(value: int | float) -> str:
    return f"Value: {value}"


print(format_value(100))
print(format_value(3.14))