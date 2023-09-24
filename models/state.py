#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref='state', cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        '''Returns the list of City instances with state_id'''
        from models import storage

        state_cities = []
        cities_dict = storage.all(City)

        for city in cities_dict.values():
            if city.state_id == self.id:
                state_cities.append(city)

        return state_cities
