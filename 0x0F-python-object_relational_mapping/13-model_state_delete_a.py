#!/usr/bin/python3
"""Write a script that deletes all State objects with a name\
containing the letter a from the database hbtn_0e_6_usa"""
from model_state import State, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import select
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        all_states = session.query(State).filter(State.name.contains('a'))

        for state in all_states:
            session.delete(state)

        session.commit()
