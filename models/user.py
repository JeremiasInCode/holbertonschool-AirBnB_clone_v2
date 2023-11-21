#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ This class defines a user by various attributes """

    storage_engine = getenv('HBNB_TYPE_STORAGE')
    if storage_engine is None:
        storage_engine = "db"

    if storage_engine == "db":
        __tablename__ = 'users'

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True, default=Null())
        last_name = Column(String(128), nullable=True, default=Null())
        places = relationship("Place", back_populates="user", cascade="delete, delete-orphan")
        reviews = relationship("Review", back_populates="user", cascade="delete, delete-orphan")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
