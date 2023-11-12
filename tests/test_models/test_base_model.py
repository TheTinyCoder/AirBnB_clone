#!/usr/bin/python3
"""
BaseModel Test Module
"""
import io
import json
import sys
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up class"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    @classmethod
    def tearDownClass(self):
        """Tear down class"""
        del self.base1
        del self.base2

    def test_instance(self):
        """Test that instance of base is initialized correctly"""
        self.assertTrue(isinstance(self.base1, BaseModel))
        self.assertTrue(isinstance(self.base2, BaseModel))
        self.assertFalse(self.base1 is self.base2)
        self.assertNotEqual(self.base1, self.base2)
        self.assertTrue(
            self.base1.id is not None and isinstance(self.base1.id, str))
        self.assertEqual(self.base1.created_at, self.base1.updated_at)
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)
        base3 = BaseModel(**self.base2.to_dict())
        self.assertFalse(self.base2 is base3)
        self.assertNotEqual(self.base2, base3)
        self.assertEqual(self.base2.id, base3.id)
        self.assertEqual(self.base2.created_at, base3.created_at)
        self.assertEqual(self.base2.updated_at, base3.updated_at)

    def test_str(self):
        """Test __str__ method"""
        sys.stdout = file = io.StringIO()
        print(self.base1)
        sys.stdout = sys.__stdout__
        expected = f"[BaseModel] ({self.base1.id}) {self.base1.__dict__}"
        self.assertEqual(expected, file.getvalue()[:-1])

    def test_save(self):
        """Test save method"""
        current_updated_at = self.base2.updated_at
        self.base2.save()
        self.assertNotEqual(current_updated_at, self.base2.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        base1_dict = self.base1.to_dict()
        self.assertIn('__class__', base1_dict.keys())
        self.assertEqual(base1_dict["id"], self.base1.id)
        self.assertEqual(
            base1_dict["__class__"], self.base1.__class__.__name__)
        try:
            datetime.strptime(base1_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("created_at was not in ISO format")
        try:
            datetime.strptime(base1_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("updated_at was not in ISO format")
