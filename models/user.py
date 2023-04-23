#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        _password = Column('password', String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete-orphan")
        reviews = relationship('Review', backref='user',
                               cascade='all, delete-orphan')
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        '''creating user instance'''
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        '''hash password'''
        self._password = password
