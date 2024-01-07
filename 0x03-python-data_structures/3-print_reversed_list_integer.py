#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    my_list.reverse()
    for j in range(i):
        print("{:d}".format(j))
