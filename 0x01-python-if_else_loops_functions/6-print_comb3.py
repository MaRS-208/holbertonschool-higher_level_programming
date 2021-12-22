#!/usr/bin/python3
for c in range(0, 10):
    for s in range(0, 10):
        if c < s:
            print("{}{}".format(c, s), end="")
            if c != 8:
                print(", ", end="")
print("")
