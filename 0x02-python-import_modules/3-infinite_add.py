#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    ac = len(sys.argv)
    for i in range(1, ac):
        res += int(sys.argv[i])
    print("{}".format(res))
