#!/usr/bin/python3

"""
a script that change name of State objects

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
    i = session.query(State).filter(State.id == 2).first()
    i.name = "New Mexico"
    session.add(i)
    session.commit()
    session.close()
