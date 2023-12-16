#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_MYSQL_DB") == 'db':
        cities = relationship("City", backref="state",
                          cascade='all, delete-orphan')
    else:
        def cities(self):
            from models import storage
            listOfCities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    listOfCities.append(city)
            return (listOfCities)
