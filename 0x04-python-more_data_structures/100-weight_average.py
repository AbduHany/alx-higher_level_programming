#!/usr/bin/python3
def weight_average(my_list=[]):
    if (my_list == [] or my_list is None):
        return (0)
    weightsum = 0
    tupleproduct = []
    for i in range(len(my_list)):
        weightsum += my_list[i][1]
        tupleproduct.append(my_list[i][0] * my_list[i][1])
    weightaverage = sum(tupleproduct) / weightsum
    return (weightaverage)
