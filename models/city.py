#!/usr/bin/python3
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.state import State


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        # places = relationship("Place", backref="cities",
        #                       cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""