#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""

import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Custom class for file storage
    """

    __file_path = "file.json"
    __objects = {}
    __models = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
    }

    def all(self):
        """
        Returns dictionary representation of all objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the object with the key
        <object class name>.id

        Args:
            object(obj): object to write

        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        serialised_objects = {}

        for key, obj in self.__objects.items():
            serialised_objects[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialised_objects, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                instances = json.load(file)

            for key, obj_dict in instances.items():
                class_name, obj_id = key.split(".")

                """ obj_instance = getattr(
                __import__(class_name), class_name)(**obj_dict) """
                obj_instance = self.__models[class_name](**obj_dict)

                self.__objects[key] = obj_instance
