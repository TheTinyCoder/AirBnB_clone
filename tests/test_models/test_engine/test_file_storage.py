#!/usr/bin/python3
"""
File Storage Test Module
"""
import io
import datetime
import json
import os
import sys
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up: executed before and after each test"""
        self.storage = FileStorage()

    def test_all(self):
        """Test all method"""
        model = BaseModel()
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertTrue(isinstance(self.storage.all(), dict))

    def test_new(self):
        """Test new method"""
        base_dict = {"__class__": "BaseModel",
                     "updated_at": "2017-09-28T21:07:25.047381",
                     "created_at": "2017-09-28T21:07:25.047372",
                     "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}
        model = BaseModel(**base_dict)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertFalse(key in self.storage._FileStorage__objects)
        self.storage.new(model)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_save(self):
        """Test save method"""
        self.assertFalse(os.path.exists(FileStorage._FileStorage__file_path))
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test reload method"""
        expected = len(FileStorage._FileStorage__objects)
        self.assertIsNone(self.storage.reload())
        self.assertEqual(expected, len(FileStorage._FileStorage__objects))

    def tearDown(self):
        """Tear down: executed before and after each test"""
        del self.storage
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass
