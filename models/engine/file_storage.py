#!/usr/bin/python3
"""File storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Handles serialisation and deserialisation"""

    __file_path = 'storage.json'
    __objects = {}

    def all(self):
        """Returns all objecrs"""

        return type(self).__objects

    def new(self, obj):
        """Adds a new object to our objects dict"""

        type(self).__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """Save our object dict to our file path"""

        dict_to_save = {}
        for key, val in type(self).__objects.items():
            dict_to_save[key] = val.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            json.dump(dict_to_save, f)

    def reload(self):
        """Reloads objects from file path"""

        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                dict_loaded = json.load(f)
                class_dicts = {'BaseModel': BaseModel,
                               'User': User,
                               'Place': Place,
                               'Review': Review,
                               'City': City,
                               'Amenity': Amenity,
                               'State': State,
                               }
                for key1, val in dict_loaded.items():
                    for key in class_dicts:
                        if key1[0:len(key)] == key:
                            type(self).__objects[key1] = class_dicts[key](
                                    **val)
        except FileNotFoundError:
            return
