#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
import shlex


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    name: str = ''
