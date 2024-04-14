#!/usr/bin/python3
"""This module prints all City objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, dbname
    ))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = (session.query(State.name, City.id, City.name).
              join(State).order_by(City.id).all())
    for row in result:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
