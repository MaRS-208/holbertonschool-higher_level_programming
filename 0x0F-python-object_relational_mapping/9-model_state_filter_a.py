#!/usr/bin/python3
"""Write a script that lists all State objects that\
contain the letter a from the database hbtn_0e_6_usa"""

from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:\
    {argv[2]}@localhost/{argv[3]}')
    with Session(bind=engine) as session:
        q = session.query(State).filter(State.name.contains('a')).all()
        for i in q:
            print(f'{i.id}: {i.name}')
