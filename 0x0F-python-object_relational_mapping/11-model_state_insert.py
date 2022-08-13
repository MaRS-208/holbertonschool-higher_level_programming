#!/usr/bin/python3
"""Write a script that adds the State object\
“Louisiana” to the database hbtn_0e_6_usa"""

from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:\
    {argv[2]}@localhost/{argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state = State(name='Louisiana')
        session.add(state)
        session.commit()
        print(state.id)
