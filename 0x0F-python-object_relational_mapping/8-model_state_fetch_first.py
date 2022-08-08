#!/usr/bin/python3
"""Write a script that prints the first State\
object from the database hbtn_0e_6_usa"""


from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from model_state import Base
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:\
    {argv[2]}@localhost/{argv[3]}')
    with Session(bind=engine) as session:
        q = session.query(State).first()
        print(f'{q.id}: {q.name}')
