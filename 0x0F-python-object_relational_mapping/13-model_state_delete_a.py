#!/usr/bin/python3
"""Write a script that deletes all State objects with a name\
containing the letter a from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

     with Session(engine) as session:
        all_states = session.query(State).filter(State.name.contains('a'))
        for state in all_states:
            session.delete(state)
        session.commit()
