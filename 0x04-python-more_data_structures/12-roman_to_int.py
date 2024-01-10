#!/usr/bin/python3
def roman_to_int(roman_string):
    romandict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    if (roman_string is None) or (roman_string == ""):
        return (0)
    elif (isinstance(roman_string, str) == False):
        return (0)
    num = 0
    for i in range(len(roman_string)):
        num += romandict.get(roman_string[i])
        if (i + 1 < len(roman_string)):
            if (romandict.get(roman_string[i + 1])
                    > romandict.get(roman_string[i])):
                num -= (romandict.get(roman_string[i])) * 2
    return (num)
