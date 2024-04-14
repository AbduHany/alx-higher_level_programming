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
    conn = MySQLdb.connect(host='localhost', user=username,
                           passwd=password, db=dbname)
    cur = conn.cursor()
    cur.execute(('SELECT cities.id, cities.name, states.name FROM ' +
                 'cities INNER JOIN states ON states.id = cities.state_id;'))
    result = cur.fetchall()
    for row in result:
        print(row)
