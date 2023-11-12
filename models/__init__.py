#!/usr/bin/python3
"""Initializes package"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


classes = {"BaseModel": BaseModel, "FileStorage": FileStorage, "User": User}
storage = FileStorage()
storage.reload()
