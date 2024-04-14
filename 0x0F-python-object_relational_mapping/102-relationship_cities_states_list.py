#!/usr/bin/python3
"""This module lists all City objects from the database hbtn_0e_101_usa
"""
from relationship_state import Base, State
from relationship_city import City
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
    result = session.query(City).order_by(City.id).all()
    for row in result:
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))
