#!/usr/bin/python3

"""Test Cases for Sqaure Class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """Unit tests for Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_atributes(self):
        """Check if square has all rectangle attributes"""

        sq = Square(3)
        self.assertEqual(sq.height, 3)
        self.assertEqual(sq.width, 3)
        self.assertEqual(sq.id, 1)

    def test_square_inheritance(self):
        """Square is a subclass of Rectangle and Base"""

        sq2 = Square(9)
        self.assertTrue(isinstance(sq2, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(isinstance(sq2, object))

    def test_square_initialized_with_no_args(self):
        """Checks if Square initialised with  no args"""

        with self.assertRaises(TypeError) as context:
            sq = Square()
        self.assertEqual("__init__() missing 1 required positional argument: 'size'", str(context.exception))

    def test_square_represantion(self):
        """Check the str represantion of square"""

        sq1 = Square(3, 4, 5)
        self.assertEqual("[Square] (1) 4/5 - 3", str(sq1))

    def test_square_methods_inherited(self):
        """Check if Square inherited successfully all the Rectangle methods"""

        sq = Square(4)
        self.assertEqual(sq.area(), 16)

        sq.update(3)
        self.assertEqual(sq.id, 3)

        sq.update(height=3)
        self.assertEqual(sq.height, 3)

    def test_square_size_getter_and_setter(self):
        """Check if the getter and setter works properly"""

        sq = Square(12, 23, 34)
        self.assertEqual(sq.size, 12)
        sq.size = 13
        self.assertEqual(sq.size, 13)

    def test_square_size_getter_and_setter_with_wrong_values(self):
        """Check if properly validation on square size"""

        with self.assertRaises(TypeError) as context:
            sq = Square("twelve")
        self.assertEqual("width must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            sq = Square(2, "twelve", 5)
        self.assertEqual("x must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            sq = Square(2, 12, "twelve")
        self.assertEqual("y must be an integer", str(context.exception))

        with self.assertRaises(ValueError) as context:
            sq = Square(0)
        self.assertEqual("width must be > 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            sq = Square(-1)
        self.assertEqual("width must be > 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            sq = Square(12, -99, 3 )
        self.assertEqual("x must be >= 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            sq = Square(12, 3, -33 )
        self.assertEqual("y must be >= 0", str(context.exception))



    
if __name__ == '__main__':
    unittest.main()