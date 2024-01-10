#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None) or (a_dictionary == {}):
        return None
    sortedvals = list(reversed(sorted(a_dictionary.values())))
    bestscore = sortedvals[0]
    for i, j in a_dictionary.items():
        if j == bestscore:
            return (i)
