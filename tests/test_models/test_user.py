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
        self.value = User

    def test_first_name(self):
        """ test_first_name model """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test_last_name model """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test_email model """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ test_password model """
        new = self.value()
        self.assertEqual(type(new.password), str)
