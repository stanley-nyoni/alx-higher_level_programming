#!/usr/bin/python3

"""
    Module: 9-model_state_filter_a
    Lists all states containg letter 'a'
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    u_name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(u_name, pwd, db), pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_results = session.query(State) \
        .order_by(State.id).filter(State.name.like("%x%"))
    for state in state_results:
        print("{}: {}".format(state.id, state.name))
