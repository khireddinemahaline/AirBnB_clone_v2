#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
import shlex
import models

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
        
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            from models.city import City
            list_cities = []
            all_cities = models.storage.all(City)
            for key, city_obj in all_cities.items():
                if city_obj.state_id == self.id:
                    list_cities.append(city_obj)
            return list_cities
