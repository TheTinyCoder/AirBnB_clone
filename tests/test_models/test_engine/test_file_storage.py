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
    @classmethod
    def setUpClass(self):
        """Set up class"""
        self.storage = FileStorage()

    def storage_len(self):
        """Returns total number of objects in file path"""
        if (os.path.exists(FileStorage._FileStorage__file_path)):
            with open(FileStorage._FileStorage__file_path, "r") as file:
                objects = list(json.load(file).keys())
                return (len(objects))
        else:
            return (0)

    def test_all(self):
        """Test all method"""
        self.assertEqual(len(self.storage.all()), self.storage_len())
        model = BaseModel()
        model.save()
        self.assertEqual(len(self.storage.all()), self.storage_len())
"""
    def test_new(self):
        ""Test new method""
        base_dict = list(self.storage.all().values())[0].to_dict()
        model = BaseModel(**base_dict)
        current_objects = self.storage.all()
        self.storage.new(model)
        self.assertEqual(len(current_objects), len(self.storage.all()))


    def test_save(self):
        ""Test save method""
        base_dict = list(self.storage.all().values())[0].to_dict()
        model = BaseModel(**base_dict)
        self.storage.new(model)
        self.storage.save()
        if (os.path.exists(FileStorage._FileStorage__file_path)):
            with open(FileStorage._FileStorage__file_path, "r") as file:
                objects = list(json.load(file).keys())
                print(objects)
        self.assertTrue(f"BaseModel.{model.id}" in objects)
"""
    @classmethod
    def tearDownClass(self):
        """Tear dowm class"""
        os.remove(FileStorage._FileStorage__file_path)
