#!/usr/bin/python3
"""Defines engine for interacting with database"""

from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """class definition for db storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize engine"""
        # dialect+driver://username:password@host:port/database
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(user, pwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self, cls=None):
        '''Retrieve all objects or individual class objects'''

        my_classes = [User, State, City, Amenity, Place, Review]

        dictionary = {}

        if cls is not None:
            for value in self.__session.query(cls).all():
                key = '{}.{}'.format(value.__class__.__name__, value.id)
                dictionary[key] = value
        else:
            for clas in my_classes:
                for value in self.__session.query(clas).all():
                    key = '{}.{}'.format(value.__class__.__name__, value.id)
                    dictionary[key] = value

        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Calls remove() method on the private session attribute
        """
        self.__session.close()
