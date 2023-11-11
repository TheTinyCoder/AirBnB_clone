#!/usr/bin/python3
"""File Storage Module"""
import json


class FileStorage:
    """
    FileStorage Class
    Attributes:
        file_path (str: private class attribute)
        objects (dict: private class attribute)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Args:
            obj: object to add to __objects dict
        """
        if obj is not None:
            key = f"{obj.to_dict()['__class__']}.{obj.id}"
            FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects:
            only if the JSON file (__file_path) exists
            otherwise, nothing is done
        """
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                FileStorage.__objetcs = json.load(f)
        except Exception:
            pass
