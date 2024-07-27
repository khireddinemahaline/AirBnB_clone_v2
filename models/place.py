#!/usr/bin/python3
"""Place Class"""

from os import env
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Place(BaseModel, Base):
    """Place Class"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = 

    else:
        city_id: str = ''
        user_id: str = ''
        name: str = ''
        description: str = ''
        number_room: int = 0
        number_bathroom: int = 0
        max_guest: int = 0
        price_by_night: int = 0
        latitude: float = 0.0
        longitude: float = 0.0
        amenity_ids: list = {}
