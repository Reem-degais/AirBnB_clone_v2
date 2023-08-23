#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel,  Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
                "place_amenity", Base.metadata,
                Column("place_id", String(60), ForeignKey("places.id"),
                       primary_key=True, nullable=False),
                Column("amenity_id", String(60), ForeignKey("amenities.id"),
                       primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
                "Amenity", secondary="place_amenity",
                viewonly=False)
        reviews = relationship(
                "Review", backref='place',
                cascade='all, delete, delete-orphan')
    else:
        @property
        def amenities(self):
            """Getter method to retrieve the related Amenity objects.

            Returns:
                list: A list of Amenity objects associated with the place.
            """
            from models import storage
            amenity_list = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get("Amenity", amenity_id)
                if amenity:
                    amenity_list.append(amenity)
                return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """Setter method to add an Amenity object to the place's amenities.

            Args:
                obj (Amenity): The Amenity object to be added.
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """Get a list of all related review objects."""
            from models import storage
            reviews_list = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_list.append(value)
            return reviews_list
