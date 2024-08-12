#!/usr/bin/python3
"""
Contains the class DBStorage.

The DBStorage class manages interactions with a MySQL database using SQLAlchemy.
It provides methods to perform CRUD operations and manage database sessions.
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """
    Interacts with the MySQL database using SQLAlchemy.

    Attributes:
        __engine (sqlalchemy.engine.base.Engine): The SQLAlchemy engine instance.
        __session (sqlalchemy.orm.scoping.scoped_session): The scoped session factory instance.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiate a DBStorage object.

        Initializes the SQLAlchemy engine based on environment variables and
        sets up the database connection. If the environment is 'test', it
        drops all existing tables.
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all instances of a given class from the database.

        Args:
            cls (type, optional): The class of objects to query. If None, queries all classes.

        Returns:
            dict: A dictionary where the keys are formatted as "<class name>.<object id>"
                  and the values are the corresponding object instances.
        """
        db_dict = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                if obj.__class__.__name__ in models.classes:
                    db_dict[key] = obj
        return db_dict

    def new(self, obj):
        """
        Add a new object to the current database session.

        Args:
            obj (BaseModel): The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.

        This method saves all changes made to the objects in the session to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session.

        Args:
            obj (BaseModel, optional): The object to delete. If None, no operation is performed.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload data from the database and initialize the session.

        Creates all tables in the database and initializes a new scoped session.
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """
        Close the current database session.

        This method ensures that the database session is properly closed.
        """
        self.__session.close()
