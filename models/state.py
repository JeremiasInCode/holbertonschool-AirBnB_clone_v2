#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        """Returns the list of City instances"""
        from models.city import City
        from models import storage
        listed = []
        for i in storage.all(City).values():
            if i.state_id == self.id:
                listed.append(i)
        return listed
