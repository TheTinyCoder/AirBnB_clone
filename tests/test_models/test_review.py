#!/usr/bin/python3
"""
Review Test Module
"""
import io
import json
import sys
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up class"""
        self.review1 = Review()
        self.review2 = Review()

    @classmethod
    def tearDownClass(self):
        """Tear down class"""
        del self.review1
        del self.review2

    def test_instance(self):
        """Test that instance of review is initialized correctly"""
        self.assertTrue(isinstance(self.review1, Review))
        self.assertTrue(isinstance(self.review2, Review))
        self.assertFalse(self.review1 is self.review2)
        self.assertNotEqual(self.review1, self.review2)
        self.assertTrue(self.review1.place_id == "")
        self.assertTrue(self.review1.place_id == self.review1.user_id)
        self.assertTrue(self.review1.text == "")
        self.assertTrue(
            self.review1.id is not None and isinstance(self.review1.id, str))
        self.assertEqual(self.review1.created_at, self.review1.updated_at)
        self.assertNotEqual(self.review1.id, self.review2.id)
        self.assertNotEqual(self.review1.created_at, self.review2.created_at)
        review3 = Review(**self.review2.to_dict())
        self.assertFalse(self.review2 is review3)
        self.assertNotEqual(self.review2, review3)
        self.assertEqual(self.review2.id, review3.id)
        self.assertEqual(self.review2.created_at, review3.created_at)
        self.assertEqual(self.review2.updated_at, review3.updated_at)

    def test_str(self):
        """Test __str__ method"""
        sys.stdout = file = io.StringIO()
        print(self.review1)
        sys.stdout = sys.__stdout__
        expected = f"[Review] ({self.review1.id}) {self.review1.__dict__}"
        self.assertEqual(expected, file.getvalue()[:-1])

    def test_save(self):
        """Test save method"""
        current_updated_at = self.review2.updated_at
        self.review2.save()
        self.assertNotEqual(current_updated_at, self.review2.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        review1_dict = self.review1.to_dict()
        self.assertIn('__class__', review1_dict.keys())
        self.assertEqual(review1_dict["id"], self.review1.id)
        self.assertEqual(
            review1_dict["__class__"], self.review1.__class__.__name__)
        try:
            datetime.strptime(
                review1_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("created_at was not in ISO format")
        try:
            datetime.strptime(
                review1_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("updated_at was not in ISO format")
