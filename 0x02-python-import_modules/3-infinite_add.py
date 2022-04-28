#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)

    i = 0
    for indx in range(1, argc):
        i += int(argv[indx])
    print(i)
