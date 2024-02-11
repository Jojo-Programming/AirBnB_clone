#!/usr/bin/python3
"""the `review` module.

It defines one class, `Review(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """a review of a place/house.

    It represents a review posted by the users
    of the application about a place/house.

    Attributes:
        text
        user_id
        place_id
    """
    text = ""
    user_id = ""
    place_id = ""
