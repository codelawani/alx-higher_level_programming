#!/usr/bin/python3
"""This script contains the class definition of a City"""

from model_state import State, Base
from sqlalchemy.orm import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy import Column, Integer, String, ForeignKey
from sys import argv
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class City(Base):
    """Creates a city object"""
    __tablename__ = 'cities'

    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey(
        'states.id'), nullable=False)
