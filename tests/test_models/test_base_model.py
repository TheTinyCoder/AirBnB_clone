#!/usr/bin/python3
"""
BaseModel Test Module
"""
import io
import json
import sys
import unittest
from datetime import datetime
from freezegun import freeze_time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
        try:
            os.remove("file.json")
        except Exception:
            pass

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
        old_updated_at = self.base2.updated_at
        # check that datetime.now is not equal to mock date
        self.assertNotEqual(
            datetime.now(), datetime(2023, 11, 13, 21, 7, 51, 973301))
        with freeze_time("2023-11-13 21:07:51.973301"):
            # freeze time to return specific datetime
            # when datetime.now is called
            self.assertEqual(
                datetime.now(), datetime(2023, 11, 13, 21, 7, 51, 973301))
            # check that save() updates updated_at to mocked date
            expected_time = datetime.now()
            self.base2.save()
        self.assertEqual(expected_time, self.base2.updated_at)
        # check that datetime.now is no longer equal to mocked date
        self.assertNotEqual(
                datetime.now(), datetime(2023, 11, 13, 21, 7, 51, 973301))
        self.assertNotEqual(old_updated_at, self.base2.updated_at)
        key = f"{self.base2.__class__.__name__}.{self.base2.id}"
        expected = FileStorage._FileStorage__objects[key].updated_at
        self.assertEqual(expected, self.base2.updated_at)

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
