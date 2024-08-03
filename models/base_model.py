#!/usr/bin/python3
""" base model that all model will inhert from"""

import uuid
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, DateTime
import models
Base = declarative_base()



class BaseModel:
    """
    BaseModel:
        id : the uuid of the class
        created at : the time this class was created
        updated at : the time this class was uptated 
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    def __init__(self, *arg, **kwargs):
        """
        constructore that build our class
        args:
            arg: wont be used
            kwarg: new arguments for the constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if "id" not in kwargs:
                    self.id = setattr(uuid.uuid4)
                if "created_at" not in kwargs:
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                    self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        
    def to_dict(self):
        dic_obj = self.__dict__.copy()
        dic_obj["__class__"] = self.__class__.__name__
        dic_obj["created_at"] = self.created_at.isoformat()
        dic_obj["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dic_obj:
            del dic_obj["_sa_instance_state"]
        return dic_obj
    def delete():
        models.storage.delete()
