#!/usr/bin/python3
from tests.test_models.test_base_model import test_basemodel
from models.review import review

class test_review(test_review):
    """
    Tests for review model
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_text(self):
        """
        Test text
        """
        current = self.value
        self.assertEqual(type(current.text), str)

    def test_place(self):
        """
        Test place id
        """
        current = self.value
        self.assertEqual(type(current.place_id), str)

    def test_user(self):
        """
        Test user id
        """
        current = self.value
        self.assertEqual(type(current.user_id), str)
