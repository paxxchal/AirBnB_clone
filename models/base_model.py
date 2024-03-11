#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class for AirBnB clone."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save the instance to a file."""
        self.updated_at = datetime.now()
        storage.save()
        storage.new(self)

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    @classmethod
    def from_dict(cls, input_dict):
        """Create an instance from a dictionary representation."""
        if "__class__" in input_dict:
            class_name = input_dict.pop("__class__")
            if class_name == cls.__name__:
                return cls(**input_dict)
        return None
