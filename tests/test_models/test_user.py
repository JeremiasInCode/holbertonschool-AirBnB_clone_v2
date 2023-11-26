#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_user(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ __init__ method """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = user
