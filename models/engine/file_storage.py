#!/usr/bin/python3
"""Creating File Storage"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes and deserializes instances to/from a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary with objects"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Sets objects with a new object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as file:
            objs_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(objs_dict, file)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objs_dict = json.load(file)
            for key, value in objs_dict.items():
                cls_name = value["__class__"]
                if cls_name == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
                # Extend this for other classes as needed
                elif cls_name == "User":
                    FileStorage.__objects[key] = User(**value)
        except FileNotFoundError:
            pass

