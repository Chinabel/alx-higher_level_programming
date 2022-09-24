#!/usr/bin/python3
def print_arg(argv):
    if __name__ == "__main__":
        """Print the number of and list of arguments."""
        import sys

        count = len(sys.argv)
        print("{} ".format(args - 1), end="")
        if count == 1:
            print("arguments.")
        elif count > 1:
            if count == 2:
                print("argument:")
            elif count > 2:
                print("arguments:")
            for i in range(count - 1):
                print("{}: {}".format(i + 1, sys.argv[i + 1]))
