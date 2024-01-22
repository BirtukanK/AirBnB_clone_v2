#!/usr/bin/python3
""" defines the database storage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

class DBStorage:
    """ Class that defines the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of a class"""
        mysql_user = os.environ.get("HBNB_MYSQL_USER")
        mysql_password = os.environ.get("HBNB_MYSQL_PWD")
        mysql_host = os.environ.get("HBNB_MYSQL_HOST", "localhost")
        mysql_db = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(mysql_user, mysql_password, mysql_host, mysql_db), pool_pre_ping=True)
        if env == 'test':
            Base = declarative_base()
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ querys the current database session and return a dictionary"""
        objects = {}
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        for class1 in classes:
            queries = self.__session.query(class1).all()
            class_name = class1.__name__

        for query in queries:
            key = f"{class_name}.{query_id}"
            objects[key] = query

        return objects

    def new(self, obj):
        """ Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes from the current database session if obj is not none"""
        if obj is not None:
            self.__session.query(type(obj)).filter(type(obj).id == obj.id).delete(synchronize_session=False)

    def reload(self):
        """ Create all tables in the database"""
        Base = declarative_base()
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(SessionFactory)()
