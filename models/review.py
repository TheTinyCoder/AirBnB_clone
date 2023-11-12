#!/usr/bin/python3
"""Review Module"""
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class
    Attributes:
        place_id (string:  public class attribute)
        user_id (string: public class attribute)
        text (string: public class attribute)
    """
    place_id = ""
    user_id = ""
    text = ""
