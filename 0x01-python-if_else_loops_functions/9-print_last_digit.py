#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    if (number == 0):
        ret = 0
    else:
        ret = number % 10
    print(ret, end="")
    return (ret)
