#!/usr/bin/python3
"""This module creates the State `California` with the City
`San Francisco` from the database hbtn_0e_100_usa"""
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newcity = City(name='San Francisco')
    newcity.state = State(name='California')
    session.add(newcity)
    session.commit()
