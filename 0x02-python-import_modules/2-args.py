#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length < 2:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} {}:".format(length - 1, "arguments"))
        for y in range(1, length):
            print("{}: {}".format(y, sys.argv[y]))
