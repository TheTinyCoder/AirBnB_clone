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
                return (len(list(json.load(file).keys())))
        else:
            return (0)

    def test_all(self):
        """Test all method"""
        self.assertNotEqual(len(self.storage.all()), self.storage_len())
        model = BaseModel()
        model.save()
        self.assertEqual(len(self.storage.all()), self.storage_len())
 
    @classmethod
    def tearDownClass(self):
        """Tear dowm class"""
        os.remove(FileStorage._FileStorage__file_path)
