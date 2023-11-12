#!/usr/bin/python3
"""File Storage Module"""
import json
import models


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
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        objects = {}
        for (k, v) in FileStorage.__objects.items():
            objects[k] = v.to_dict()
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects:
            only if the JSON file (__file_path) exists
            otherwise, nothing is done
        """
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                for (k, v) in json.load(f).items():
                    cls = models.classes[v["__class__"]]
                    self.new(cls(**v))
        except FileNotFoundError:
            pass
