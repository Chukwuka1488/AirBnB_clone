#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes and deserializes instances to/from a JSON file"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

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
        except FileNotFoundError:
            pass

