#!/usr/bin/python3
"""User Class"""


from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
