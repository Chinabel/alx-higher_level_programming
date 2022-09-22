#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argv_count = len(argv) - 1
    operators = ["+", "-", "*", "/"]
    if argv_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        sys.argv = argv[2]
        b = int(sys.argv[3])
        if sys.argv[2] is "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif sys.argv[2] is "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif sys.argv[2] is "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif sys.argv[2] is "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
