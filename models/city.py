#!/usr/bin/python3
"""City Class"""

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """city Class"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60),  ForeignKey('states.id'), nullable=False,)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
