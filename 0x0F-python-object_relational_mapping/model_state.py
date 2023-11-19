#!/usr/bin/python3

"""
    Module: model_state.py
    contains the class definition of a State
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

# connection_string = "mysql+mysqldb://"
# engine = create_engine()
Base = declarative_base()


class State(Base):
    """Initialize a state class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
