#!/usr/bin/python3
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_place(test_basemodel):
    """ test_place class """
    def __init__(self, *args, **kwargs):
        """ __init__ method """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test_city_id model """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ test_user_id model """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test_name model """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test_name description """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test_number_rooms model """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test_number_bathrooms model """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test_max_guest model """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test_prince_by_night model """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test_latitude model """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test_longitude model """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ test_amenity_ids """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
