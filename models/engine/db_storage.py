#!/usr/bin/python3
"""data base storage file"""

from os import getenv
from sqlalchemy import create_engine, MetaData
from models.base_model import BaseModel
from sqlalchemy.orm import sessionmaker
from models.state import State
from models.city import City


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                    .format(user, pwd, host,db)
                                    , pool_pre_ping=True)
        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        db_dict = {}

        if cls != "":
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dict[key] = obj
            return db_dict

    def new(self, obj):
        self.__session.add(obj)
    def save(self):
        self.__session.commit()
    def delete(self, obj=None):
        self.__session.delete(obj)
    def reload(self):
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
    def close(self):
        self.__session.close()
