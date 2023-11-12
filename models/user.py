#!/usr/bin/python3
"""User Module"""
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class
    Attributes:
        email (string):  public class attribute)
        password (string: public class attribute)
        first_name (string: public class attribute)
        last_name (string: public class attribute)

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
