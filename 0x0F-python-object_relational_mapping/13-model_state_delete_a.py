#!/usr/bin/python3
"""Write a script that deletes all State objects with a name\
containing the letter a from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)
    from model_state import Base
    from model_state import State
    from sys import argv

    engine = create_engine(f'mysql+mysqldb://{argv[1]}:\
    {argv[2]}@localhost/{argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    fsession = Session(engine)
    for state in session.query(State).filter(\
        State.name.contains('a')):
        session.delete(state)
    session.commit()
    session.close()
