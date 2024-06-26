#!/usr/bin/python3
"""storage file"""


import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """FileStorage Class : manipulate dictionary save and reload"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """set a key to obj"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """deserializes __objects to the JSON file (path: __file_path)"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "State": State,
            "Place": Place,
            "Review": Review
        }
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    name = k.split('.')[0]
                    if name in classes:
                        obj = classes[name](**v)
                        self.__class__.__objects[k] = obj
