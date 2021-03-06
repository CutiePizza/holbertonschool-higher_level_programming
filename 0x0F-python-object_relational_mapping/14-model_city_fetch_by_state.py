#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for row1, row2 in session.query(City, State).filter(
            City.state_id == State.id
            ).order_by(City.id).all():
        print("{}: ({}) {}".format(row2.name, row1.id, row1.name))
