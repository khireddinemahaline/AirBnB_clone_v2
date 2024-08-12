#!/usr/bin/python3
"""Base model that all models will inherit from.

This module provides a base class `BaseModel` for all models, including 
both file and database storage systems. It defines common attributes and 
methods for all models.

Imports:
    - uuid: For generating unique identifiers.
    - declarative_base: Base class for SQLAlchemy models.
    - datetime: For handling date and time.
    - Column, String, DateTime: SQLAlchemy column types.
    - models: For accessing the storage engine.

Attributes:
    id (str): The unique identifier for an instance.
    created_at (datetime): The timestamp when the instance was created.
    updated_at (datetime): The timestamp when the instance was last updated.

Methods:
    __init__(*arg, **kwargs):
        Constructor that initializes the attributes.
        Args:
            *arg: Unused positional arguments.
            **kwargs: Keyword arguments to initialize attributes.
    __str__():
        Returns a string representation of the instance.
    save():
        Updates the `updated_at` timestamp and saves the instance to storage.
    to_dict():
        Returns a dictionary representation of the instance.
    delete():
        Deletes the instance from storage (this method is not implemented).

The `BaseModel` class is used as a base class for all models to ensure 
consistency and provide common functionality.
"""

import uuid
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, DateTime
import models

Base = declarative_base()

class BaseModel:
    """
    BaseModel:
        id: The UUID of the class instance.
        created_at: The time when this class instance was created.
        updated_at: The time when this class instance was last updated.
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *arg, **kwargs):
        """
        Constructor that initializes the class instance.
        
        Args:
            *arg: Unused positional arguments.
            **kwargs: Keyword arguments to set attribute values.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance."""
        cls = type(self).__name__  # Extracts the name of the class
        attributes = ', '.join(f"'{key}': {repr(getattr(self, key))}" 
                               for key in self.__dict__.keys() 
                               if key != '_sa_instance_state')
        return f"[{cls}] ({self.id}) {{{attributes}}}"

    def save(self):
        """Updates the `updated_at` timestamp and saves the instance to storage."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dic_obj = {}
        dic_obj.update(self.__dict__)
        if '_sa_instance_state' in dic_obj:
            del (dic_obj['_sa_instance_state'])
        dic_obj.update({'__class__': (str(type(self)).split('.')[-1]).split('\'')[0]})
        dic_obj['created_at'] = self.created_at.isoformat()
        dic_obj['updated_at'] = self.updated_at.isoformat()
        return dic_obj

    def delete(self):
        """Deletes the instance from storage."""
        models.storage.delete()
