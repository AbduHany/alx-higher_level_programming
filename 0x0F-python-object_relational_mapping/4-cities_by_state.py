#!/usr/bin/python3
"""This module defines a python program that
lists all cities from the database hbtn_0e_4_usa.
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
    cur.execute(('SELECT cities.id, cities.name, states.name FROM ' +
                 'cities INNER JOIN states ON states.id = cities.state_id;'))
    result = cur.fetchall()
    for row in result:
        print(row)
