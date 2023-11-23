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
    else:
        print("Function not implemented.")
        sys.exit(1)


if __name__ == "__main__":
    function_number = parse_command_line()
    print(f"Selected function number: {function_number}")

    # Define x values
    xval = np.arange(-3.0, 3.0, 0.1).tolist()

    # Initialize y values
    yval = []

    # Fill lists based on function number
    fill_lists_irrational(xval, yval, function_number)

    print("xval:", xval)
    print("yval:", yval)


