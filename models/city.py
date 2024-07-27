#!/usr/bin/python3
"""City Class"""

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import Relationship
from models.places import Place 


class City(BaseModel, Base):
    """city Class"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60),  ForeignKey('states.id'), nullable=False,)
        name = Column(String(128), nullable=False)
        places = Relationship("Place", backref='cities', cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
