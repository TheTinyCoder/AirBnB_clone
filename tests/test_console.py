#!/usr/bin/python3
"""
Console Test Module
"""
import sys
import unittest
from console import HBNBCommand
from io import StringIO
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Test the console"""
    def setUp(self):
        """Set up: run before each function"""
        self.backup = sys.__stdout__
        self.file = StringIO()
        sys.stdout = self.file
        self.objects = FileStorage._FileStorage__objects

    def tearDown(self):
        """Tear down: run after each function"""
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

    def test_help(self):
        expected = ['\n', 'Documented commands (type help <topic>):',
                    '\n', '========================================',
                    '\n', 'EOF  all  count  create  destroy  help  ',
                    'quit  show  update', '\n']
        console = self.create()
        console.onecmd('help')
        self.assertEqual(self.file.getvalue()[:-1], "".join(expected))

    def test_empty_line(self):
        """Test that emptyline executes nothing"""
        console = self.create()
        console.onecmd('\n')
        self.assertTrue(len(self.file.getvalue()) == 0)

    def test_create(self):
        """Test that create function creates an instance and prints id"""
        console = self.create()
        console.onecmd("create BaseModel")
        self.assertTrue(
            "BaseModel." + self.file.getvalue()[:-1] in self.objects.keys())

    def test_all(self):
        """Test all method"""
        console = self.create()
        sys.stdout= self.backup
        console.onecmd("create User")
        console.onecmd("create City")
        console.onecmd("create State")
        console.onecmd("create Place")
        console.onecmd("create Review")
        console.onecmd("all")
        self.assertTrue(isinstance(self.file.getvalue(), str))
        sys.stdout = self.file
        console.onecmd("all BaseModel")
        objects = self.file.getvalue().replace('\n', '').split('[')
        objects = [i for i in objects if i!= '']
        self.assertTrue(all("BaseModel" in i for i in objects))
        sys.stdout = self.backup
        self.file.close()
        self.file = StringIO()
        sys.stdout = self.file
        console.onecmd("City.all()")
        objects = self.file.getvalue().replace('\n', '').split('[')
        objects = [i for i in objects if i!= '']
        self.assertTrue(all("City" in i for i in objects))

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
