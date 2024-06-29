#!/usr/bin/python3
"""base model"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """Base Model for creating and managing instances"""
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """save atrrubuite instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """converte objects to string"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """convert objects to dictionarry so we could manipulate with json"""
        dic_obj = self.__dict__.copy()
        dic_obj['__class__'] = self.__class__.__name__
        dic_obj['created_at'] = self.created_at.isoformat()
        dic_obj["updated_at"] = self.updated_at.isoformat()
        return dic_obj
