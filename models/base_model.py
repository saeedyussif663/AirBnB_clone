#!/usr/bin/python3
import uuid
from datetime import datetime

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
    def __init__(self):
        """initialization function"""
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def __str__(self):
        """str method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the object"""
        self.updated_at = str(datetime.now())

    def to_dict(self):
        """returns the attribute """
        return self.__dict__
