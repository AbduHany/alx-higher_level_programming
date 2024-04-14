#!/usr/bin/python3
"""This module defines a python program that  displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    searchname = sys.argv[4]
    conn = MySQLdb.connect(host='localhost', user=username,
                           passwd=password, db=dbname)
    cur = conn.cursor()
    stmt = ("SELECT * FROM states WHERE name " +
            "LIKE '{}' COLLATE utf8mb4_bin ORDER BY id ASC".format(searchname))
    cur.execute(stmt)
    result = cur.fetchall()
    for row in result:
        print(row)
