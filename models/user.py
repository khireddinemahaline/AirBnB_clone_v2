#!/usr/bin/python3
"""User Class"""

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.places import Places
from sqlalchemy.orm import Relationship



class User(BaseModel, Base):
    """User Class"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = Relationship("Place", backref='users', cascade="all, delete, delete-orphan")
    else:
        email: str = ''
        password: str = ''
        first_name: str = ''
        last_name: str = ''
