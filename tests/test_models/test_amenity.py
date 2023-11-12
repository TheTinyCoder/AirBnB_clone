#!/usr/bin/python3
"""
Amenity Test Module
"""
import io
import json
import sys
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up class"""
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()

    @classmethod
    def tearDownClass(self):
        """Tear down class"""
        del self.amenity1
        del self.amenity2

    def test_instance(self):
        """Test that instance of amenity is initialized correctly"""
        self.assertTrue(isinstance(self.amenity1, Amenity))
        self.assertTrue(isinstance(self.amenity2, Amenity))
        self.assertFalse(self.amenity1 is self.amenity2)
        self.assertNotEqual(self.amenity1, self.amenity2)
        self.assertTrue(self.amenity1.name == "")
        self.assertTrue(
            self.amenity1.id is not None and isinstance(self.amenity1.id, str))
        self.assertEqual(self.amenity1.created_at, self.amenity1.updated_at)
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)
        self.assertNotEqual(self.amenity1.created_at, self.amenity2.created_at)
        amenity3 = Amenity(**self.amenity2.to_dict())
        self.assertFalse(self.amenity2 is amenity3)
        self.assertNotEqual(self.amenity2, amenity3)
        self.assertEqual(self.amenity2.id, amenity3.id)
        self.assertEqual(self.amenity2.created_at, amenity3.created_at)
        self.assertEqual(self.amenity2.updated_at, amenity3.updated_at)

    def test_str(self):
        """Test __str__ method"""
        sys.stdout = file = io.StringIO()
        print(self.amenity1)
        sys.stdout = sys.__stdout__
        expected = f"[Amenity] ({self.amenity1.id}) {self.amenity1.__dict__}"
        self.assertEqual(expected, file.getvalue()[:-1])

    def test_save(self):
        """Test save method"""
        current_updated_at = self.amenity2.updated_at
        self.amenity2.save()
        self.assertNotEqual(current_updated_at, self.amenity2.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        amenity1_dict = self.amenity1.to_dict()
        self.assertIn('__class__', amenity1_dict.keys())
        self.assertEqual(amenity1_dict["id"], self.amenity1.id)
        self.assertEqual(
            amenity1_dict["__class__"], self.amenity1.__class__.__name__)
        try:
            datetime.strptime(
                amenity1_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("created_at was not in ISO format")
        try:
            datetime.strptime(
                amenity1_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("updated_at was not in ISO format")
