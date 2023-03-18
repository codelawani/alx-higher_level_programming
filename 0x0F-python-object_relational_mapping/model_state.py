#!/usr/bin/python3
"""
a script that contains the class definition of a State
and an instance Base = declarative_base()
"""
import sys
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy import (create_engine)

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)


class State(Base):
    """creates a state object"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
