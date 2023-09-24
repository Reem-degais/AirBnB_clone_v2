#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ The State class which has relationship with the City class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    """else:
        name = ''"""

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            from models import storage
            city_list = []
            city_dict = models.storage.all(models.City)
            for value, key in city_dict.items():
                if self.id == value.state_id:
                    city_list.append(value)
            return city_list
