#!/usr/bin/python3
"""
FileStorage module

This module defines the `FileStorage` class, which is responsible for
storing and retrieving objects in a JSON file. It implements methods
to manage and persist objects to the file system, providing functionality
to create, read, update, and delete objects
"""

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
    This class manages storage of objects in a JSON file.

    Attributes:
        __file_path (str): The file path to the JSON file where objects are stored.
        __objects (dict): A dictionary of all objects stored in memory.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or objects of a specified class.

        If cls is provided, it filters objects by class. If cls is None, returns all objects.

        Args:
            cls (type or str, optional): The class type or class name to filter objects by.

        Returns:
            dict: A dictionary where keys are formatted as "<class name>.<object id>" 
                  and values are the corresponding object instances.
        """
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
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to be added to storage.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves all objects to the JSON file.

        Serializes __objects to JSON format and writes them to the file specified by __file_path.
        """
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            my_dict = {}
            my_dict.update(FileStorage.__objects)
            for key, value in my_dict.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """
        Loads data from the JSON file and deserializes it into __objects.

        Reads the JSON file and creates objects based on the data in the file.
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                obj = self.__objects[key]
                obj = models.classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from storage.

        If obj is not None, the specified object is removed from __objects.

        Args:
            obj (BaseModel, optional): The object to be deleted from storage.
        """
        if obj is not None:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            FileStorage.__objects.pop(key, None)
            self.save()

    def close(self):
        """
        Closes the storage by calling reload().

        This method reloads the data, which is equivalent to deserializing the JSON file.
        """
        self.reload()
