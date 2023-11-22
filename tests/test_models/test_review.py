#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ test_review class """

    def __init__(self, *args, **kwargs):
        """ __init__ method """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test_place_id model """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test_user_id model """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test_text model """
        new = self.value()
        self.assertEqual(type(new.text), str)
