#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    cities = relationship("City", back_populates='places')
    user = relationship("User", back_populates="places", cascade='delete')
    reviews = relationship("Review", cascade='delete', back_populates='place')

    @property
    def amenities(self):
        '''returns the amenity_ids'''
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        '''
        handles append method for adding an Amenity.id
        to the attribute amenity_ids
        '''
        from models.amenity import Amenity
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        @property
        def amenities(self):
            """Returns the amenities of this Place"""
            from models import storage
            amenities_of_place = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_of_place.append(value)
            return amenities_of_place

        @amenities.setter
        def amenities(self, value):
            """Adds an amenity to this Place"""
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)
