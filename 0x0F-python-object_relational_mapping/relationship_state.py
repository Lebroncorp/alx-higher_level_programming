#!/usr/bin/python3

"""
Defines a State model.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
    Represents a city of a MySQL database.
    Attributes:
    "id" that represents a column of an auto-generated, unique integer,
    can’t be null and is a primary key. is the city's unique id.

    "name" that represents a column of a string of 128 characters
    and can’t be null. the city's name.

    "state_id" that represents a column of an integer,
    can’t be null and is a foreign key to states.id. the city's state unique id
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
