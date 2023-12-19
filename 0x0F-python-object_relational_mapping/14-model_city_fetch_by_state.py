#!/usr/bin/python3

"""
prints all City objects from the database hbtn_0e_14_usa:
    takes 3 arguments: mysql username, mysql password and database name.
    Results must be sorted in ascending order by cities.id.
    Results must be display as they are in the example below
    (<state name>: (<city id>) <city name>).
"""

import sys
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
            .filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
