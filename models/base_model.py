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


    ## this __str__ method is where your error did came from and i have modified it.
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__ # this extracts the name of the instance of the class
        ## the var <attributes> stores the values of all the attributes in that class instance
        ## except _sa_instance_state
        attributes = ', '.join(f"'{key}': {repr(getattr(self, key))}" for key in self.__dict__.keys() if key != '_sa_instance_state')
        return f"[{cls}] ({self.id}) {{{attributes}}}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        
    def to_dict(self):
        dic_obj = {}
        dic_obj.update(self.__dict__)
        if '_sa_instance_state' in dic_obj:
            del (dic_obj['_sa_instance_state'])
        dic_obj.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dic_obj['created_at'] = self.created_at.isoformat()
        dic_obj['updated_at'] = self.updated_at.isoformat()
        return dic_obj
    def delete():
        models.storage.delete()
