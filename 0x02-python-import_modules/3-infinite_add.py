#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    """print the addition of all the argument."""
    total = 0
    for i in (len(sys.argv) - 1):
    total += int(sys.argv[i + 1])
    print("{}".format(result))
