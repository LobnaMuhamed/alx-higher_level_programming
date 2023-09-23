#!/usr/bin/python3

"""
a script that lists all State objects

from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in (session.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id)):
        print(item[0] + ": (" + str(item[1]) + ") " + item[2])

    session.close()
