#!/usr/bin/python3
"""
Script that lists all State
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).filter(
            State.name == sys.argv[4]
            )
    if len(query.all()) == 0:
        print("Not found")
    else:
        for row in session.query(State).order_by(State.id).filter(
                State.name == sys.argv[4]
                ):
            print(row.id)
