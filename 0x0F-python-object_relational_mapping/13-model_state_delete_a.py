#!/usr/bin/python3
"""Write a script that deletes all State objects with a name\
containing the letter a from the database hbtn_0e_6_usa"""


if __name__ == "__main__":


    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from sys import argv

    engine = create_engine(f'mysql+mysqldb://{argv[1]}:\
    {argv[2]}@localhost/{argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with  Session(engine) as session:
    q = select(State).filter(State.name.contains('a'))
    r = session.execute(q).all()
    for row in r:
        session.delete(row[0])
    session.commit()
    session.close()
