#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if (len_a == 0):
        a_0 = 0
        a_1 = 0
    elif (len_a == 1):
        a_0 = tuple_a[0]
        a_1 = 0
    else:
        a_0 = tuple_a[0]
        a_1 = tuple_a[1]
    if (len_b == 0):
        b_0 = 0
        b_1 = 0
    elif (len_b == 1):
        b_0 = tuple_b[0]
        b_1 = 0
    else:
        b_0 = tuple_b[0]
        b_1 = tuple_b[1]
    sumtup = (a_0 + b_0, a_1 + b_1)
    return (sumtup)
