#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='delete')
    # @property
    # def cities(self):
    #     '''Returns the lists of the City instances'''
    #     from models import storage
    #     from models.city import City
    #     dict_cities = storage.all(City)
    #     list_cities = []

    #     for value in dict_cities.values():
    #         if value.state_id == self.id:
    #             list_cities.append(value)
    #     return list_cities
