#!/usr/bin/python3
num = 122
for i in range(0, 26):
    if (i == 0):
        pass
    elif ((i % 2) == 0):
        num = num - 1 + 32
    else:
        num = num - 1 - 32
    print("{}".format(chr(num)), end="")
