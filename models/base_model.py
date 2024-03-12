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
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(
                            self, key, datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # models.storage.new(self)

    def __str__(self):
        """str method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the object"""
        self.updated_at = datetime.now()
        # models.storage.save()

    def to_dict(self):
        """returns the attribute """
        model_dict = self.__dict__.copy()

        model_dict["__class__"] = self.__class__.__name__
        model_dict["updated_at"] = self.updated_at.isoformat()
        model_dict["created_at"] = self.created_at.isoformat()

        return model_dict
