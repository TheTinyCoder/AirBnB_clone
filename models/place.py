#!/usr/bin/python3
"""Place Module"""
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Class
    Attributes:
        city_id (string:  public class attribute)
        user_id (string:  public class attribute)
        name (string:  public class attribute)
        description (string:  public class attribute)
        number_rooms (int:  public class attribute)
        number_bathrooms (int:  public class attribute)
        max_guest (int:  public class attribute)
        price_by_night (int:  public class attribute)
        latitude (float:  public class attribute)
        longitude (float:  public class attribute)
        amenity_ids (list of strings: public class attribute)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
