#!/usr/bin/python3
""" Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City """

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id):
        for city in session.query(City).filter(
                City.state_id == state.id).order_by(City.id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
