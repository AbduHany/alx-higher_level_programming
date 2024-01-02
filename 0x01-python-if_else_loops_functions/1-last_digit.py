#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if ((number % 10) == 0):
    lastdig = 0
elif (number < 0):
    lastdig = (number % 10) - 10
else:
    lastdig = number % 10
print(f"Last digit of {number} is {lastdig} and is ", end="")
if (lastdig == 0):
    print("0")
elif (lastdig > 5):
    print("greater than 5")
else:
    print("less than 6 and not 0")
