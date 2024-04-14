#!/usr/bin/python3
"""This module defines a python program that takes in the name of
a state as an argument and lists all cities of that state, using
the database hbtn_0e_4_usa.
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
