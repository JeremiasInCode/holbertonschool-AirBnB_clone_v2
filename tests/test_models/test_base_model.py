#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        current = self.value()
        copy_class = current.to_dict()
        data_intance = BaseModel(**copy_class)
        self.assertFalse(data_intance is copy_class)

    def test_kwargs_int(self):
        """ """
        current = self.value()
        copy = current.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError): data_instance = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        current = self.value()
        current.save()
        key = self.name + "." + current.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], current.to_dict())

    def test_str(self):
        """ """
        current = self.value()
        self.assertEqual(str(current), '[{}] ({}) {}'.format(self.name, current.id,
                         current.__dict__))

    def test_todict(self):
        """ """
        current = self.value()
        dict_instance = current.to_dict()
        self.assertEqual(current.to_dict(), dict_instance)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError): new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError): new = self.value(**n)

    def test_created_at(self):
        """ """
        current = self.value()
        self.assertEqual(type(current.created_at), datetime.datetime)
