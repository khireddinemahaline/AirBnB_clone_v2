#!/usr/bin/python3
"""storage file"""


import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State



class FileStorage:
    """
    store data in file storage
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__objects
    def new(self, obj):
        """
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
    def save(self):
        """
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)
    def reload(self):
        """
        """
        with open(self.__file_path, 'r',encoding="UTF-8") as f:
            for key, value in (json.load(f).items()):
                value = eval(value["__class__"])(**value)
                self.__objects[key] = value
    