#!/usr/bin/python3
"""
City Test Module
"""
import io
import json
import sys
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up class"""
        self.city1 = City()
        self.city2 = City()

    @classmethod
    def tearDownClass(self):
        """Tear down class"""
        del self.city1
        del self.city2

    def test_instance(self):
        """Test that instance of city is initialized correctly"""
        self.assertTrue(isinstance(self.city1, City))
        self.assertTrue(isinstance(self.city2, City))
        self.assertFalse(self.city1 is self.city2)
        self.assertNotEqual(self.city1, self.city2)
        self.assertTrue(self.city1.state_id == "")
        self.assertTrue(self.city1.name == "")
        self.assertTrue(
            self.city1.id is not None and isinstance(self.city1.id, str))
        self.assertEqual(self.city1.created_at, self.city1.updated_at)
        self.assertNotEqual(self.city1.id, self.city2.id)
        self.assertNotEqual(self.city1.created_at, self.city2.created_at)
        city3 = City(**self.city2.to_dict())
        self.assertFalse(self.city2 is city3)
        self.assertNotEqual(self.city2, city3)
        self.assertEqual(self.city2.id, city3.id)
        self.assertEqual(self.city2.created_at, city3.created_at)
        self.assertEqual(self.city2.updated_at, city3.updated_at)

    def test_str(self):
        """Test __str__ method"""
        sys.stdout = file = io.StringIO()
        print(self.city1)
        sys.stdout = sys.__stdout__
        expected = f"[City] ({self.city1.id}) {self.city1.__dict__}"
        self.assertEqual(expected, file.getvalue()[:-1])

    def test_save(self):
        """Test save method"""
        current_updated_at = self.city2.updated_at
        self.city2.save()
        self.assertNotEqual(current_updated_at, self.city2.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        city1_dict = self.city1.to_dict()
        self.assertIn('__class__', city1_dict.keys())
        self.assertEqual(city1_dict["id"], self.city1.id)
        self.assertEqual(
            city1_dict["__class__"], self.city1.__class__.__name__)
        try:
            datetime.strptime(city1_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("created_at was not in ISO format")
        try:
            datetime.strptime(city1_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("updated_at was not in ISO format")
