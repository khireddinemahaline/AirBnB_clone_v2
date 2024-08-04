#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    else:
        name: str = ''
