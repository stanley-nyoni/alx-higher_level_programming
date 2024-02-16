#!/usr/bin/python3

"""
    Module: model_state.py
    contains the class definition of a State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
