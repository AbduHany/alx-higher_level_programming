#!/usr/bin/python3
"""This module defines a script that reads stdin linebyline and computes
metrics for the lines read.
"""
if __name__ == "__main__":
    import sys

    def print_stats(totalsize, errordict):
        print("File size: {}".format(totalsize))
        for key in sorted(errordict.keys()):
            if errordict[key] == 0:
                continue
            print("{}: {}".format(key, errordict[key]))

    errordict = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    i = 0
    totalsize = 0
    try:
        for line in sys.stdin:
            if ((i % 10) == 0) and (i != 0):
                print_stats(totalsize, errordict)
            singleline = line.split()
            try:
                totalsize += int(singleline[-1])
            except Exception:
                pass
            if (singleline[-2] in list(errordict.keys())):
                errordict[singleline[-2]] += 1
            i += 1
        print_stats(totalsize, errordict)
    except KeyboardInterrupt:
        print_stats(totalsize, errordict)
        raise
