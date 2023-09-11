#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    argv = sys.argv
    argc = len(argv)

    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        i = argv[1]
        j = argv[3]
        operand = argv[2]

        if (operand == "+"):
            print("{} + {} = {}".format(i, j, add(int(i), int(j))))
        elif (operand == "-"):
            print("{} - {} = {}".format(i, j, sub(int(i), int(j))))
        elif (operand == "*"):
            print("{} * {} = {}".format(i, j, mul(int(i), int(j))))
        elif (operand == "/"):
            print("{} / {} = {}".format(i, j, div(int(i), int(j))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
