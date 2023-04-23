#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
        citites = relationship('City', cascade="all, delete",
                               backref='states')
    else:
        name = ""

        @property
        def cities(self):
            '''getter attribute that returns city objects'''
            city_value = models.storage.all(City).values()
            list_city = []
            for city in city_value:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city

    def __init__(self, *args, **kwargs):
        '''initializes state'''
        super().__init__(*args, **kwargs)
