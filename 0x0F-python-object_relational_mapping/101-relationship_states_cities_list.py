#!/usr/bin/python3

"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
take 3 arguments: mysql username, mysql password and database name.
Results must be sorted in ascending order by states.id and cities.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
