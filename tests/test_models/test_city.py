#!/usr/bin/python3
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_city(test_basemodel):
    """ Tests for city model """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test state_id """
        current = self.value
        self.assertEqual(type(current.state_id), str)

    def test_name(self):
        """ Test name """
        current = self.value
        self.assertEqual(type(current.name), str)
