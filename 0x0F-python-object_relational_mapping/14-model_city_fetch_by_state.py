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
    cities_list = session.query(City, State)\
                         .filter(City.state_id == State.id)\
                         .order_by(City.id)\
                         .all()
    for state, city in cities_list:
        print("{}: ({}) {}".format(city.name, state.id, state.name))
    session.close()
