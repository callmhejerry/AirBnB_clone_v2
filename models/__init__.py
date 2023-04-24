#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


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
