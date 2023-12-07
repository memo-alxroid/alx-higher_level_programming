#!/usr/bin/python3

if __name__ == "__main__":
    """Print arguments and their numbers"""
    import sys
    if len(sys.argv) == 1:
        print("{}".format(0))
    elif len(sys.argv) == 2:
        print("{}".format(int(sys.argv[1])))
    else:
        sumarg = 0
        for i in range(len(sys.argv)):
            if i == 0:
                continue
            number = int(sys.argv[i])
            sumarg += number
        print("{}".format(int(sumarg)))
