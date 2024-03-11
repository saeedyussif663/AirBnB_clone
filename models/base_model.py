#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""Base class
- Public instance attribute
    id: unique identifier
    created_at: datetime of when instance was created
    updated_at: datetime of when instance was updated

- Public instance methods
    save(self): updates the public instance attribute updated_at
    to_dict(self): returns a dictionary containing all
            keys/values of __dict__ of the instance

- str: string representation
"""


class BaseModel():
    """Base class"""
    def __init__(self, *args, **kwargs):
        """initialization function"""
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """str method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the object"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns the attribute """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.strptime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
