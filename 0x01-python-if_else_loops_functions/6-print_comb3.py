#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        print("{:02d}, ".format(i), end="")
    elif ((i % 10) == 0):
        i += (i + 1)
        continue
    elif (i == 89):
        print("{:02d}".format(i))
        break
    else:
        print("{:02d}, ".format(i), end="")
