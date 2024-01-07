#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if ((my_list is None) or (len(my_list)) == 0):
        return None
    divisiblelist = []
    for i in my_list:
        if ((i % 2) == 0):
            divisiblelist.append(True)
        else:
            divisiblelist.append(False)
    return (divisiblelist)
