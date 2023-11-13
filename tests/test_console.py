#!/usr/bin/python3
"""
Console Test Module
"""
import sys
import unittest
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test the console"""
    def setUp(self):
        """Set up"""
        self.backup = sys.__stdout__
        self.file = StringIO()
        sys.stdout = self.file

    def tearDown(self):
        """Tear down"""
        sys.stdout = self.backup

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
        sys.stdout = file = StringIO()
        console.onecmd('\n')
        sys.stdout = sys.__stdout__
        self.assertTrue(len(file.getvalue()) == 0)

    def test_all(self):
        """Test all exists"""
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.file.getvalue(), str))

    def test_show(self):
        """Testing that show exists"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.file.getvalue()
        sys.stdout = self.backup
        self.file.close()
        self.file = StringIO()
        sys.stdout = self.file
        console.onecmd("show User " + user_id)
        x = (self.file.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    def test_show_class_name(self):
        """Testing the error messages for class name missing"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.file.getvalue()
        sys.stdout = self.backup
        self.file.close()
        self.file = StringIO()
        sys.stdout = self.file
        console.onecmd("show")
        x = (self.file.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def test_show_class_name(self):
        """Test show message error for id missing"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.file.getvalue()
        sys.stdout = self.backup
        self.file.close()
        self.file = StringIO()
        sys.stdout = self.file
        console.onecmd("show User")
        x = (self.file.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    def test_show_no_instance_found(self):
        """Test show message error for id missing"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.file.getvalue()
        sys.stdout = self.backup
        self.file.close()
        self.file = StringIO()
        sys.stdout = self.file
        console.onecmd("show User " + "124356876")
        x = (self.file.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create(self):
        """Test that create works"""
        console = self.create()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.file.getvalue(), str))

    def test_class_name(self):
        """Testing the error messages for class name missing"""
        console = self.create()
        console.onecmd("create")
        x = (self.file.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_class_name_doest_exist(self):
        """Testing the error messages for class name missing"""
        console = self.create()
        console.onecmd("create Binita")
        x = (self.file.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)
