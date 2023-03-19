#!/usr/bin/python3
"""This script lists all State objects that contain the letter a from the
database hbtn_0e_6_usa"""
from model_state import State, Base
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    for i in states:
        print(f'{i.id}: {i.name}')
    session.close()
