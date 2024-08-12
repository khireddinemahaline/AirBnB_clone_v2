#!/usr/bin/python3
"""storage file"""


import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


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
        """create new obj"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ save new object"""
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            my_dict = {}
            my_dict.update(FileStorage.__objects)
            for key, value in my_dict.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                obj = self.__objects[key]
                obj = models.classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''
        Deletes an obj
        '''
        if obj is not None:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            FileStorage.__objects.pop(key, None)
            self.save()

    def close(self):
        '''
        Deserialize JSON file to objects
        '''
        self.reload()
