#!/usr/bin/python3
"""City Class"""


from models.base_model import BaseModel, Base
from sqlaichemy import Column, String


class City(BaseModel, Base):
    """city Class"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
