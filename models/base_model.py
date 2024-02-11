#!/usr/bin/python3
"""Base model module"""
import uuid
import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialises the BaseModel class"""
    if kwargs:
    for key, val in kwargs.items():
    if key != '__class__':
    if key == 'created_at' or key == 'updated_at':
    setattr(self, key, datetime.datetime.fromisoformat(val))
        else:
            setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of instance"""
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Saves an instance"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the dict representation of a BaseModel"""
        class_dict = {}
        for key, val in self.__dict__.items():
            class_dict[key] = val
        class_dict['__class__'] = type(self).__name__
        class_dict['created_at'] = class_dict['created_at'].isoformat(
                timespec='microseconds')
        class_dict['updated_at'] = class_dict['updated_at'].isoformat(
                timespec='microseconds')
        return class_dict
