#!/usr/bin/python3
"""Write a script that deletes all State objects with a name\
containing the letter a from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine, select
    from sqlalchemy.orm import Session

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    mysql_db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_user, mysql_pass, mysql_db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = select(State).filter(State.name.ilike('%a%'))
        result = session.execute(query).all()
        for row in result:
            session.delete(row[0])
        session.commit()
