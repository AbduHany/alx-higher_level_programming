#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if ((length == 0) or (my_list is None)):
        return
    if ((idx < 0) or (idx > (length - 1))):
        return (my_list)
    del my_list[idx]
    return (my_list)
