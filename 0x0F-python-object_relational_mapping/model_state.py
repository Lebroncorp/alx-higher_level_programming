#!/usr/bin/pyhton3

"""
Defines a State model.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state.
    __tablename__ (str): The name of the MySQL table to store the States.
    id: The state's id.
    name: The state's name.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
