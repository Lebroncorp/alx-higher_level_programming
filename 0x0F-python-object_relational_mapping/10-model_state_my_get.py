#!/usr/bin/python3

"""
Prints the State object passed as argument from database hbtn_0e_6_usa.
Takes 4 arguments: mysql username, mysql password, database name
and state name to search.
SQL injection free
Results must display the states.id.
If no state has the name you searched for, display Not found
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    found = False

    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")
