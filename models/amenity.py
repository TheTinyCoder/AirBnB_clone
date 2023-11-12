#!/usr/bin/python3
"""Amenity Module"""
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class
    Attributes:
        name (string: public class attribute)
    """
    name = ""
