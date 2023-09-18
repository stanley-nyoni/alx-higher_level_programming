#!/usr/bin/python3

"""
    Unit tests for Base class
"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test Class for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_id(self):
        """Check the id for new instance of Base object"""

        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base(9).id, 9)
        self.assertEqual(Base(567).id, 567)

    def test_type_and_instance(self):
        """Check the type and instance of Base objects"""

        base1 = Base(23)
        self.assertEqual(type(base1), Base)
        self.assertTrue(isinstance(base1, Base))

        




if __name__ == '__main__':
    unittest.main()