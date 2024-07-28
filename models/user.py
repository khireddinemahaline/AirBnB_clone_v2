#!/usr/bin/python3
"""User Class"""

from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """User Class"""
    __tablename__ = 'users'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user", cascade="all, delete, delete-orphan")
    else:
        email: str = ''
        password: str = ''
        first_name: str = ''
        last_name: str = ''
