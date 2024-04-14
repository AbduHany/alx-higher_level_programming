#!/usr/bin/python3
"""This module prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
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
    result = (session.query(State).filter(State.name.ilike('%a%')).
              order_by(State.id).all())
    if result:
        for row in result:
            print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
