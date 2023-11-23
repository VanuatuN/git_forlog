# Stage 1: Handle Command Line

import sys
import numpy as np
import matplotlib.pyplot as plt
import math


def parse_command_line():
    if len(sys.argv) != 2:
        print("Usage: python script.py <function_number>")
        sys.exit(1)
    
    try:
        function_number = int(sys.argv[1])
        return function_number
    except ValueError:
        print("Please provide a valid integer for function number.")
        sys.exit(1)


def fill_lists_irrational(xval, yval, function_number):
    if function_number == 1:
        yval.extend(xval)  # y = f(x) = x
    elif function_number == 2:
        yval.extend(x**2 for x in xval)  # y = f(x) = x**2
    elif function_number == 3:
        yval.extend(x**3 for x in xval)  # y = f(x) = x**3
    elif function_number == 4:
        yval.extend(math.sin(x) for x in xval)  # y = f(x) = sin(x)
    elif function_number == 5:
        yval.extend(math.cos(x) for x in xval)  # y = f(x) = cos(x)
    elif function_number == 6:
        yval.extend(math.tan(x) for x in xval)  # y = f(x) = tan(x)
    elif function_number == 7:
        yval.extend(math.exp(x) for x in xval)  # y = f(x) = exp(x)
    else:
        print("Function not implemented.")
        sys.exit(1)


if __name__ == "__main__":
    function_number = parse_command_line()
    print(f"Selected function number: {function_number}")

    # Define x values
    xval = np.arange(-5.0, 5.0, 0.1).tolist()

    # Initialize y values
    yval = []

    # Fill lists based on function number
    fill_lists_irrational(xval, yval, function_number)

    print("xval:", xval)
    print("yval:", yval)


