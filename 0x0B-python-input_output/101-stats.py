#!/usr/bin/python3
"""This module defines a script that reads stdin linebyline and computes
metrics for the lines read.
"""
import sys

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
        singleline = line.split()
        totalsize += int(singleline[-1])
        if (singleline[-2] in list(errordict.keys())):
            errordict[singleline[-2]] += 1
        i += 1
        if ((i % 10) == 0):
            print("File size: {}".format(totalsize))
            for errornum, num in errordict.items():
                if num == 0:
                    continue
                print("{}: {}".format(errornum, num))
except KeyboardInterrupt:
        print("File size: {}".format(totalsize))
        for errornum, num in errordict.items():
            if num == 0:
                continue
            print("{}: {}".format(errornum, num))
