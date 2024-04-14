#!/usr/bin/python3
"""This module defines the class City and the declarative instance Base.
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """This class defines the mapper class for the cities tables
    in the hbtn_0e_14_usa DB.
    """
    __tablename__ = "cities"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'))
