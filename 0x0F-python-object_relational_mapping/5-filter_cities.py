#!/usr/bin/python3
"""This module defines a python program that  displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
safely (without SQL Injections).
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    statename = sys.argv[4]
    conn = MySQLdb.connect(host='localhost', user=username,
                           passwd=password, db=dbname)
    cur = conn.cursor()
    stmt = ("SELECT cities.name FROM cities INNER JOIN " +
            "states ON cities.state_id = states.id WHERE states.name = %s")
    cur.execute(stmt, (statename, ))
    result = cur.fetchall()
    arr = []
    for row in result:
        for city in row:
            arr.append(city)
    if (len(arr) == 0):
        print()
    else:
        for i in range(len(arr)):
            if (i == (len(arr) - 1)):
                print(arr[i])
            else:
                print(arr[i], end=", ")
