#!/usr/bin/python3

"""
a script that deletes all State objects with name contain 'a'

from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)
    session.commit()
    session.close()
