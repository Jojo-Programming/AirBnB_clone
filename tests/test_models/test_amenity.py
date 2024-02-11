#!/usr/bin/python3
"""unit tests for the `amenity` module.
"""
import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """to test cases for the `Amenity` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """this resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """to test method for class attributes"""

        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        a3 = Amenity("hello", "wait", "in")

        k = f"{type(a1).__name__}.{a1.id}"
        self.assertIsInstance(a1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(a3.name, "")

    def test_init(self):
        """to test method for public instances"""
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        self.assertIsInstance(a1.id, str)
        self.assertIsInstance(a1.created_at, datetime)
        self.assertIsInstance(a1.updated_at, datetime)
        self.assertEqual(a1.updated_at, a2.updated_at)

    def test_str(self):
        """to test method for str representation"""
        a1 = Amenity()
        string = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
        self.assertEqual(a1.__str__(), string)

    def test_save(self):
        """to test method for save"""
        a1 = Amenity()
        old_update = a1.updated_at
        a1.save()
        self.assertNotEqual(a1.updated_at, old_update)

    def test_todict(self):
        """to test method for dict"""
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        a_dict = a2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(a2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(a1, a2)


if __name__ == "__main__":
    unittest.main()
