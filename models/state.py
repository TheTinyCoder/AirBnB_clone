#!/usr/bin/python3
"""State Module"""
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class
    Attributes:
        name (string: public class attribute)
    """
    name = ""
