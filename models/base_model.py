#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import getenv
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at
        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    val = datetime.fromisoformat(val)
                setattr(self, key, val)

        """
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
            # storage.new(self)
        """

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(
            cls, self.id, {
                k: v for k, v in self.to_dict().items() if k != '__class__'})

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return {k: v for k, v in dictionary.items() if k !=
                "_sa_instance_state"}

    def delete(self):
        """Deletes the instance from storage"""
        from models import storage
        storage.delete(self)
