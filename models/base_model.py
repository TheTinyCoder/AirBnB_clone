#!/usr/bin/python3
"""Base Model Module"""
import uuid
import datetime


class BaseModel:
    """
    BaseModel Class
    Attributes:
        id (string (uuid):  public instance attribute)
        created_at (datetime: public instance attribute)
        updated_at (datetime: public instance attribute)
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        current_time = datetime.datetime.now()
        self.created_at = current_time
        self.updated_at = current_time

    def __str__(self):
        """Returns informal string representation of class instance"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance:
            a key __class__ is added to this dict with the class name
            created_at and updated_at are converted to string in ISO format
        """

        a_dict = self.__dict__.copy()
        a_dict["__class__"] = self.__class__.__name__
        a_dict["created_at"] = self.created_at.isoformat()
        a_dict["updated_at"] = self.updated_at.isoformat()
        return (a_dict)