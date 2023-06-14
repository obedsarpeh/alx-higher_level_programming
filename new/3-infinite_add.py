#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    newsum = 0
    for i in range(len(sys.argv) - 1):
        newsum += int(sys.argv[i + 1])
    print("{}".format(newsum))
