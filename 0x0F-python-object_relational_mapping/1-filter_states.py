#!/usr/bin/python3
"""This module defines a python program that lists all states with a
name starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    conn = MySQLdb.connect(host='localhost', user=username,
                           passwd=password, db=dbname)
    cur = conn.cursor()
    stmt = ("SELECT * FROM states WHERE name " +
            "LIKE 'N%' COLLATE utf8mb4_bin ORDER BY id ASC")
    cur.execute(stmt)
    result = cur.fetchall()
    for row in result:
        print(row)
