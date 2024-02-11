#!/usr/bin/python3
"""the `city` module

It defines one class, `City(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """the city in the application.

    Attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
