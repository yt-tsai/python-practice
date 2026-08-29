# 1) Import the module
# import calculator


# result_1 = calculator.add(9, 24)
# result_2 = calculator.subtract(9, 24)


# 2) Import specific functions from the module
# from calculator import add, subtract

# result_1 = add(9, 24)
# result_2 = subtract(9, 24)


# 3) Import a module with an alias
# import calculator as calc

# result_1 = calc.add(9, 24)
# result_2 = calc.subtract(9, 24)

# print(result_1)
# print(result_2)

import calculator
# from utilities import math_tools
from utilities.math_tools import multiply, divide


def main():
    result_1 = calculator.add(9, 24)
    result_2 = calculator.subtract(9, 24)

    print(result_1)
    print(result_2)

    # Package of utilities
    # result_3 = math_tools.multiply(9, 24)
    # result_4 = math_tools.divide(9, 24)
    result_3 = multiply(9, 24)
    result_4 = divide(9, 24)

    print(result_3)
    print(result_4)


if __name__ == "__main__":
    main()