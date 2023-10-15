#!/usr/bin/python3
"""Creating base model class"""
import uuid
from datetime import datetime


class BaseModel:
    """ Base model class with public instance attributes and methods """

    def __init__(self, *args, **kwargs):
        """ Initialization of BaseModel instance """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert str representation of datetime to datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # Lazy import
            from models import storage
            storage.new(self)

    def __str__(self):
        """ String representation of BaseModel instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates updated_at with current datetime """
        self.updated_at = datetime.now()
        # Lazy import
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of BaseModel """
        base_model_dict = self.__dict__.copy()
        base_model_dict["__class__"] = self.__class__.__name__
        base_model_dict["created_at"] = self.created_at.isoformat()
        base_model_dict["updated_at"] = self.updated_at.isoformat()
        return base_model_dict

