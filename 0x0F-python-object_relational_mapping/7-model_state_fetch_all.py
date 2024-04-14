#!/usr/bin/python3
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    username, password, dbname
))
Session = sessionmaker(bind=engine)
session = Session()
result = session.query(State).order_by(State.id).all()
for row in result:
    print("{}: {}".format(row.id, row.name))
