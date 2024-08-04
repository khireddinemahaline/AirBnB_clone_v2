#!/usr/bin/python3
"""Place Class"""


from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'), primary_key=True),
        Column('amenity_id', String(60), ForeignKey("amenities.id", onupdate='CASCADE',
                                            ondelete='CASCADE'), primary_key=True))


class Place(BaseModel, Base):
    """Place Class"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False,
                                 back_populates="place_amenities")
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

        @property
        def reviews():
            """list reviews"""
            list_reviews = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            '''
                Return list: amenity inst's if Amenity.place_id=curr place.id
                FileStorage many to many relationship between Place and Amenity
            '''
            list_amenities = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, amenity=None):
            '''
                Set list: amenity instances if Amenity.place_id==curr place.id
                Set by adding instance objs to amenity_ids attribute in Place
            '''
            if amenity:
                for amenity in models.storage.all(Amenity).values():
                    if amenity.place_id == self.id:
                        amenity_ids.append(amenity)
