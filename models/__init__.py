#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage
from .amenity import Amenity
from .base_model import BaseModel
from .city import City
from .place import Place
from .review import Review
from .user import User
from .state import State

storage = None
if getenv("HBNB_TYPE_STORAGE") == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()

__all__ = [
           'Amenity',
           'BaseModel',
           'City',
           'Place',
           'Review',
           'User',
           'State',
           'storage'
           ]
