def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# When main.py imports this module, the top-level code is executed.
# print("calculator.py is running")


# If calculator.py is executed directly, __name__ is "__main__".
# If calculator.py is imported as a module, __name__ is "calculator".
#print(__name__)

# Verify the behavior described above.
if __name__ == "__main__":
    print("calculator.py is running directly")