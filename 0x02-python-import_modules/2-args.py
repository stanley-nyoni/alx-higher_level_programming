#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv)
    if ac == 1:
        print("{} arguments.".format(ac - 1))
    elif ac == 2:
        print("{} argument:".format(ac - 1))
    else:
        print("{} arguments:".format(ac - 1))
    for i in range(1, ac):
        print("{}: {}".format(i, sys.argv[i]))
