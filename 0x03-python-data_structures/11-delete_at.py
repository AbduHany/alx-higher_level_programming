#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if ((length == 0)):
        return
    elif (my_list is None):
        return
    elif ((idx < 0) or (idx > (length - 1))):
        return (my_list)
    else:
        del my_list[idx]
        return (my_list)
