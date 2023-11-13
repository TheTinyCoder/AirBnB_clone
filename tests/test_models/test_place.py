#!/usr/bin/python3
"""
Place Test Module
"""
import io
import json
import sys
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up class"""
        self.place1 = Place()
        self.place2 = Place()

    @classmethod
    def tearDownClass(self):
        """Tear down class"""
        del self.place1
        del self.place2

    def test_instance(self):
        """Test that instance of place is initialized correctly"""
        self.assertTrue(isinstance(self.place1, Place))
        self.assertTrue(isinstance(self.place2, Place))
        self.assertFalse(self.place1 is self.place2)
        self.assertNotEqual(self.place1, self.place2)
        self.assertTrue(self.place1.city_id == "")
        self.assertTrue(self.place1.city_id == self.place1.user_id)
        self.assertTrue(self.place1.name == "")
        self.assertTrue(self.place1.name == self.place1.description)
        self.assertTrue(self.place1.number_rooms == 0)
        self.assertTrue(
            self.place1.number_rooms == self.place1.number_bathrooms)
        self.assertTrue(self.place1.max_guest == 0)
        self.assertTrue(self.place1.max_guest == self.place1.price_by_night)
        self.assertTrue(self.place1.latitude == 0.0)
        self.assertTrue(self.place1.latitude == self.place1.longitude)
        self.assertTrue(isinstance(self.place1.amenity_ids, list))
        self.assertTrue(
            self.place1.id is not None and isinstance(self.place1.id, str))
        self.assertEqual(self.place1.created_at, self.place1.updated_at)
        self.assertNotEqual(self.place1.id, self.place2.id)
        self.assertNotEqual(self.place1.created_at, self.place2.created_at)
        place3 = Place(**self.place2.to_dict())
        self.assertFalse(self.place2 is place3)
        self.assertNotEqual(self.place2, place3)
        self.assertEqual(self.place2.id, place3.id)
        self.assertEqual(self.place2.created_at, place3.created_at)
        self.assertEqual(self.place2.updated_at, place3.updated_at)

    def test_str(self):
        """Test __str__ method"""
        sys.stdout = file = io.StringIO()
        print(self.place1)
        sys.stdout = sys.__stdout__
        expected = f"[Place] ({self.place1.id}) {self.place1.__dict__}"
        self.assertEqual(expected, file.getvalue()[:-1])

    def test_save(self):
        """Test save method"""
        current_updated_at = self.place2.updated_at
        self.place2.save()
        self.assertNotEqual(current_updated_at, self.place2.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        place1_dict = self.place1.to_dict()
        self.assertIn('__class__', place1_dict.keys())
        self.assertEqual(place1_dict["id"], self.place1.id)
        self.assertEqual(
            place1_dict["__class__"], self.place1.__class__.__name__)
        try:
            datetime.strptime(
                place1_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("created_at was not in ISO format")
        try:
            datetime.strptime(
                place1_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("updated_at was not in ISO format")
