#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("0")
    else:
        sum = 0
        for y in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[y])
        print(sum)
