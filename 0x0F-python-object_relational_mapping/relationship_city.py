#!/usr/bin/python3

"""
Defines a City model.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
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

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
