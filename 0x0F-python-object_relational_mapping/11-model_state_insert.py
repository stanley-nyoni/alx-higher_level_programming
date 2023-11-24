#!/usr/bin/python3

"""
    Module: 11-model_state_insert
    Adds state to the database
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

    state_to_add = State(name="Louisiana")
    session.add(state_to_add)
    session.commit()

    state = session.query(State).filter(State.name == "Louisiana").first()
    print(state.id)
