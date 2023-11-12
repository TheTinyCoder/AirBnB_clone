#!/usr/bin/python3
"""
State Test Module
"""
import io
import json
import sys
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up class"""
        self.state1 = State()
        self.state2 = State()

    @classmethod
    def tearDownClass(self):
        """Tear down class"""
        del self.state1
        del self.state2

    def test_instance(self):
        """Test that instance of state is initialized correctly"""
        self.assertTrue(isinstance(self.state1, State))
        self.assertTrue(isinstance(self.state2, State))
        self.assertFalse(self.state1 is self.state2)
        self.assertNotEqual(self.state1, self.state2)
        self.assertTrue(self.state1.name == "")
        self.assertTrue(
            self.state1.id is not None and isinstance(self.state1.id, str))
        self.assertEqual(self.state1.created_at, self.state1.updated_at)
        self.assertNotEqual(self.state1.id, self.state2.id)
        self.assertNotEqual(self.state1.created_at, self.state2.created_at)
        state3 = State(**self.state2.to_dict())
        self.assertFalse(self.state2 is state3)
        self.assertNotEqual(self.state2, state3)
        self.assertEqual(self.state2.id, state3.id)
        self.assertEqual(self.state2.created_at, state3.created_at)
        self.assertEqual(self.state2.updated_at, state3.updated_at)

    def test_str(self):
        """Test __str__ method"""
        sys.stdout = file = io.StringIO()
        print(self.state1)
        sys.stdout = sys.__stdout__
        expected = f"[State] ({self.state1.id}) {self.state1.__dict__}"
        self.assertEqual(expected, file.getvalue()[:-1])

    def test_save(self):
        """Test save method"""
        current_updated_at = self.state2.updated_at
        self.state2.save()
        self.assertNotEqual(current_updated_at, self.state2.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        state1_dict = self.state1.to_dict()
        self.assertIn('__class__', state1_dict.keys())
        self.assertEqual(state1_dict["id"], self.state1.id)
        self.assertEqual(
            state1_dict["__class__"], self.state1.__class__.__name__)
        try:
            datetime.strptime(
                state1_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("created_at was not in ISO format")
        try:
            datetime.strptime(
                state1_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("updated_at was not in ISO format")
