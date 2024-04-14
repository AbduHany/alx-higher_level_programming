#!/usr/bin/python3
"""This module changes the name of a State object from
the database hbtn_0e_6_usa
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
    state_to_change = session.query(State).filter(State.id == 2).one()
    state_to_change.name = "New Mexico"
    session.commit()
