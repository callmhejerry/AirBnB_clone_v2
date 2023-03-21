#!/usr/bin/python3

'''
The Database Engine
'''


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        '''instantiate a database engine'''
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv('HBNB_MYSQL_DB')

        url = "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, db)

        self.__engine = create_engine(url, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)

        self.__session = Session()

    def all(self, cls=None):
        '''Retrieves all objects depending of the class name given'''
        objs = None
        if cls is None:
            objs = self.__session.query().all()
        else:
            print("printing class")
            objs = self.__session.query(eval(cls)).all()

        dct = {}
        for obj in objs:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            dct[key] = obj
        return dct

    def new(self, obj):
        '''Adds a new object to the database'''
        self.__session.add(obj)

    def save(self):
        '''Commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''deletes the current database session obj if not None'''

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''creates all tables in the database'''
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
