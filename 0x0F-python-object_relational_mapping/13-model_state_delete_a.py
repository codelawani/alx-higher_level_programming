#!/usr/bin/python3
"""This script deletes all State objects with a name containing the letter a"""
from model_state import State, Base
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name.like('%a%')).all()
    for row in result:
        session.delete(row)
    session.commit()
    session.close()
