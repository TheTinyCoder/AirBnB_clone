#!/usr/bin/python3
"""City Module"""
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class
    Attributes:
        state_id (string:  public class attribute)
        name (string: public class attribute)
    """
    state_id = ""
    name = ""
