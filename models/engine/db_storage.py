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


