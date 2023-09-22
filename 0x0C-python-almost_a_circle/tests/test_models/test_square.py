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

    def test_square_update_args(self):
        """Check upacking args for square attributes"""

        sq = Square(23, 3, 5)
        self.assertEqual("[Square] (1) 3/5 - 23", str(sq))

        sq.update(23)
        self.assertEqual("[Square] (23) 3/5 - 23", str(sq))

        sq.update(23, 9)
        self.assertEqual("[Square] (23) 3/5 - 9", str(sq))

        sq.update(23, 9, 11)
        self.assertEqual("[Square] (23) 11/5 - 9", str(sq))

        sq.update(23, 9, 11, 6)
        self.assertEqual("[Square] (23) 11/6 - 9", str(sq))

        with self.assertRaises(TypeError) as context:
            sq.update("two")
        self.assertEqual("id must be an integer", str(context.exception))


    def test_square_update_kwargs(self):
        """Check unpacking kwargs for square attributes"""

        sq = Square(10)
        sq.update(id=2)
        self.assertEqual(sq.id, 2)

        with self.assertRaises(TypeError) as context:
            sq.update(id="two")
        self.assertEqual("id must be an integer", str(context.exception))

        sq.update(x=99, y=88)
        self.assertEqual("[Square] (2) 99/88 - 10", str(sq))

        sq.update(id=11, size=12, x=13, y=14)
        self.assertEqual(sq.size, 12)
        self.assertEqual(sq.id, 11)
        self.assertEqual(sq.y, 14)
        self.assertEqual(sq.x, 13)

    def test_square_to_dictionary(self):
        """Check Square dictionary represantion"""

        sq = Square(15, 25, 20)
        self.assertEqual("[Square] (1) 25/20 - 15", str(sq))

        sq_dict = sq.to_dictionary()
        self.assertEqual("{'id': 1, 'x': 25, 'y': 20, 'size': 15}", str(sq_dict))
        self.assertEqual(type(sq_dict), dict)
        self.assertEqual(sq_dict["x"], sq.x)
        self.assertEqual(sq_dict["y"], sq.y)
        self.assertEqual(sq_dict["id"], sq.id)
    
    def test_square_to_dictionary_unpacking(self):
        """Unpacking a dictionary represantion of Square to update another Square object"""

        sq = Square(10, 20, 30)
        sq_dict = sq.to_dictionary()

        sq1 = Square(1, 2, 3)
        sq1.update(**sq_dict)
        self.assertEqual(sq1.x, sq.x)
        self.assertEqual(sq_dict["x"], sq1.x)
        self.assertTrue(type(sq1), object)
        self.assertFalse(sq == sq1)




if __name__ == '__main__':
    unittest.main()