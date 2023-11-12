#!/usr/bin/python3
"""
User Test Module
"""
import io
import json
import sys
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up class"""
        self.user1 = User()
        self.user2 = User()

    @classmethod
    def tearDownClass(self):
        """Tear down class"""
        del self.user1
        del self.user2

    def test_instance(self):
        """Test that instance of user is initialized correctly"""
        self.assertTrue(isinstance(self.user1, User))
        self.assertTrue(isinstance(self.user2, User))
        self.assertFalse(self.user1 is self.user2)
        self.assertNotEqual(self.user1, self.user2)
        self.assertTrue(self.user1.email == "")
        self.assertTrue(self.user1.email == self.user1.password)
        self.assertTrue(self.user1.first_name == "")
        self.assertTrue(self.user1.first_name == self.user1.last_name)
        self.assertTrue(
            self.user1.id is not None and isinstance(self.user1.id, str))
        self.assertEqual(self.user1.created_at, self.user1.updated_at)
        self.assertNotEqual(self.user1.id, self.user2.id)
        self.assertNotEqual(self.user1.created_at, self.user2.created_at)
        user3 = User(**self.user2.to_dict())
        self.assertFalse(self.user2 is user3)
        self.assertNotEqual(self.user2, user3)
        self.assertEqual(self.user2.id, user3.id)
        self.assertEqual(self.user2.created_at, user3.created_at)
        self.assertEqual(self.user2.updated_at, user3.updated_at)

    def test_str(self):
        """Test __str__ method"""
        sys.stdout = file = io.StringIO()
        print(self.user1)
        sys.stdout = sys.__stdout__
        expected = f"[User] ({self.user1.id}) {self.user1.__dict__}"
        self.assertEqual(expected, file.getvalue()[:-1])

    def test_save(self):
        """Test save method"""
        current_updated_at = self.user2.updated_at
        self.user2.save()
        self.assertNotEqual(current_updated_at, self.user2.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        user1_dict = self.user1.to_dict()
        self.assertIn('__class__', user1_dict.keys())
        self.assertEqual(user1_dict["id"], self.user1.id)
        self.assertEqual(
            user1_dict["__class__"], self.user1.__class__.__name__)
        try:
            datetime.strptime(user1_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("created_at was not in ISO format")
        try:
            datetime.strptime(user1_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("updated_at was not in ISO format")
