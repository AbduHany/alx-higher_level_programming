"""This module defines the class State and the instance Base.
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class State(Base):
    """This class defines the mapper class for the states tables
    in the hbtn_0e_6_usa DB.
    """
    __tablename__ = "states"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
