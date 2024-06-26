#!/usr/bin/python3
"""City Class"""


from models.base_model import BaseModel


class City(BaseModel):
    """city Class"""
    state_id: str = ''
    name: str = ''
