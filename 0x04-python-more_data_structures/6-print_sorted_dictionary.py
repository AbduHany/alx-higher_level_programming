#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedkeys = sorted(list(a_dictionary))
    for i in sortedkeys:
        print("{}: {}".format(i, a_dictionary[i]))
