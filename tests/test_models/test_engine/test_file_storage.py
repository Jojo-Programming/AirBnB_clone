#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
"""Tests the base_model module"""


storage = FileStorage()


class TestBaseModel(unittest.TestCase):
    """Test base_model class"""

    def test_all(self):
        self.assertEqual(models.storage.all(), {})
        myModel = BaseModel()
        objects = {}
        objects[f'BaseModel.{myModel.id}'] = myModel
        self.assertEqual(models.storage.all(), objects)
        del models.storage.all()[f'BaseModel.{myModel.id}']
        models.storage.save()

    def test_new(self):
        myModel = BaseModel()
        self.assertEqual(myModel, models.storage.all()[
            f'BaseModel.{myModel.id}'])
        del models.storage.all()[f'BaseModel.{myModel.id}']
        models.storage.save()

    def test_saveAndReload(self):
        myModel = BaseModel()
        store = FileStorage()
        store.reload()
        self.assertEqual(myModel, store.all()[f'BaseModel.{myModel.id}'])
        del models.storage.all()[f'BaseModel.{myModel.id}']
        models.storage.save()
        self.assertEqual(models.storage.all(), {})
