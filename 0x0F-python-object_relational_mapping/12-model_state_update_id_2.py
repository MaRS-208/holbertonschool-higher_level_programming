#!/usr/bin/python3
"""Write a script that changes the name of a\
State object from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)
    from sqlalchemy import select 
    from model_state import Base
    from model_state import State
    from sys import argv

    engine = create_engine(f'mysql+mysqldb://{argv[1]}:\
    {argv[2]}@localhost/{argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        q = select(State).filter(State.id == 2)
        r = session.execute(q).first()
        if r is not None:
            r[0].name = 'New Mexico'
            session.commit()
