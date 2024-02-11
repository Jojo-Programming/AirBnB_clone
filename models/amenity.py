#!/usr/bin/python3
"""the `amenity` module

It defines one class, `Amenity(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """an amenity provided by a place/house.

    Attributes:
        name
    """

    name = ""
