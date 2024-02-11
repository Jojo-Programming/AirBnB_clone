#!/usr/bin/python3
from console import HBNBCommand
import unittest


class TestConsole(unittest.TestCase):
    """Test the console"""

    def test_all(self):
        arg = 'BaseModel'
        self.assertEqual(HBNBCommand().do_all_list(arg), [])
