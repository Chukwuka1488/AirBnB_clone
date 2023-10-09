#!/usr/bin/python3
""" Base model class"""

import uuid
from datetime import datetime


class BaseModel:
    """ Base model class with public instance attributes and methods """

    def __init__(self):
        """ Initialization of BaseModel instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ String representation of BaseModel instance """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """ Updates updated_at with current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary representation of BaseModel """
        base_model_dict = self.__dict__.copy()
        base_model_dict["__class__"] = self.__class__.__name__
        base_model_dict["created_at"] = self.created_at.isoformat()
        base_model_dict["updated_at"] = self.updated_at.isoformat()
        return base_model_dict


