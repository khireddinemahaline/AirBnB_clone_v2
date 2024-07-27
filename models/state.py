#!/usr/bin/python3
"""State Class"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """State Class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
