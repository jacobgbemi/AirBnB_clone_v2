#!/usr/bin/python3
""" Amenity Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
# from os import getenv
# from models.base_model import BaseModel, Base
# from models.place import place_amenity
# from sqlalchemy import Column, String, Integer
# from sqlalchemy import Float, ForeignKey
# from sqlalchemy.orm import relationship
# from models.amenity import Amenity
# from models.review import Review
# import models import storage


# class Amenity(BaseModel, Base):
#     '''
#         Implementation for the Amenities.
#     '''
#     __tablename__ = "places"
#     city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
#     user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
#     name = Column(String(128), nullable=False)
#     description = Column(String(1024))
#     number_rooms = Column(Integer, default=0)
#     number_bathrooms = Column(Integer, default=0)
#     max_guest = Column(Integer, default=0)
#     price_by_night = Column(Integer, default=0)
#     latitude = Column(Float)
#     longitude = Column(Float)
#     reviews = relationship("Review", backref="place", cascade="delete")
#     amenities = relationship("Amenity", secondary="place_amenity",
#                              viewonly=False)
#     amenity_ids = []

#     if getenv("HBNB_TYPE_STORAGE", None) != "db":
#         @property
#         def reviews(self):
#             """Get a list of all linked Reviews."""
#             review_list = []
#             for review in list(models.storage.all(Review).values()):
#                 if review.place_id == self.id:
#                     review_list.append(review)
#             return review_list

#         @property
#         def amenities(self):
#             """Get/set linked Amenities."""
#             amenity_list = []
#             for amenity in list(models.storage.all(Amenity).values()):
#                 if amenity.id in self.amenity_ids:
#                     amenity_list.append(amenity)
#             return amenity_list

#         @amenities.setter
#         def amenities(self, value):
#             if type(value) == Amenity:
#                 self.amenity_ids.append(value.id)