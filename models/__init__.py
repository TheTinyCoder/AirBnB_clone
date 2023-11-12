#!/usr/bin/python3
"""Initializes package"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()
classes = {"BaseModel": BaseModel, "FileStorage": FileStorage}
