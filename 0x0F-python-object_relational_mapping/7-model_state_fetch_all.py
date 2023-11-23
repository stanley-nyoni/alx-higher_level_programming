#!/usr/bin/python3

"""
    Module: 7-model_state_fetch_all
    Lists all states
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database), pool_pre_ping=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

results = session.query(State).order_by(State.id).all()
for r in results:
    print("{}: {}".format(r.id, r.name))
