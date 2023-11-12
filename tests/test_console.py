#!/usr/bin/python3
"""
Console Test Module
"""
import io
import sys
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def create(self):
        """Create an instance of HBNBCommand"""
        return HBNBCommand()

    def test_quit(self):
        """Test that quit implementation exists"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """Test that EOF implementation exists"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_empty_line(self):
        """Test that emptyline executes nothing"""
        console = self.create()
        sys.stdout = file = io.StringIO()
        console.onecmd('\n')
        sys.stdout = sys.__stdout__
        self.assertTrue(len(file.getvalue()) == 0)
