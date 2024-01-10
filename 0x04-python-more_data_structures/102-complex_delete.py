#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dicttup = list(a_dictionary.items())
    if (value in a_dictionary.values()):
        for i in range(len(dicttup)):
            if (dicttup[i][1] == value):
                del a_dictionary[dicttup[i][0]]
    return (a_dictionary)
