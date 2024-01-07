#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    list_copy = my_list.copy()
    i = len(my_list) - 1
    if (idx < 0):
        return list_copy
    elif (idx > i):
        return list_copy
    else:
        list_copy[idx] = element
        return list_copy
