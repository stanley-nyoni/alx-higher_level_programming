#!/usr/bin/python3

"""
    Unit tests for Rectangle class that inherits from Base
"""


import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for the Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_id(self):
        """Check the ids for newly instanciated rectangle objects"""

        self.assertEqual(Rectangle(1, 2).id, 1)
        self.assertEqual(Rectangle(3, 5).id, 2)
        self.assertEqual(Rectangle(6, 11).id, 3)
        self.assertEqual(Rectangle(8, 7, 0, 0, 4).id, 4)
        self.assertEqual(Rectangle(8, 7, 4, 2, 64).id, 64)
        self.assertEqual(Rectangle(8, 7, 8, 6, -4).id, -4)

    def test_rectangle_attributes_values(self):
        """Check if arguments passed assigned to their respective attribute"""

        rect1 = Rectangle(1, 3)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 3)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

        rect2 = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(rect2.width, 10)
        self.assertEqual(rect2.height, 20)
        self.assertEqual(rect2.x, 30)
        self.assertEqual(rect2.y, 40)
        self.assertEqual(rect2.id, 50)

    def test_getters_and_setters(self):
        """Instanciate Rectangle, and try to change and retrive 
            attributes using getters and setters
        """

        rect3 = Rectangle(10, 20, 30, 40, 50)

        rect3.width = 3
        self.assertEqual(rect3.width, 3)
        rect3.height = 4
        self.assertEqual(rect3.height, 4)
        rect3.x = 5
        self.assertEqual(rect3.x, 5)
        rect3.y = 6
        self.assertEqual(rect3.y, 6)
        rect3.id = 7
        self.assertEqual(rect3.id, 7)

    def test_constructor_with_not_enough_args(self):
        """Check if constructor raises TypeError, for missing args"""

        with self.assertRaises(TypeError):
            rect4 = Rectangle(1)

        with self.assertRaises(TypeError):
            rect4 = Rectangle(0)

        with self.assertRaises(TypeError):
            rect4 = Rectangle(-1)

    def test_validated_attributes(self):
        """Check if attributes are assigned with well-validated values"""

        with self.assertRaises(TypeError) as context:
            rect5 = Rectangle("One", 2)
        self.assertEqual("width must be an integer", str(context.exception))
        
        with self.assertRaises(TypeError) as context:
            rect5 = Rectangle(1, "two")
        self.assertEqual("height must be an integer", str(context.exception))
        
        with self.assertRaises(TypeError) as context:
            rect5 = Rectangle(1, 2, "three", 4, 5)
        self.assertEqual("x must be an integer", str(context.exception))
        
        with self.assertRaises(TypeError) as context:
            rect5 = Rectangle(1, 2, 3, "four", 5)
        self.assertEqual("y must be an integer", str(context.exception))

    def test_validated_value_errors(self):
        """Check if properly considered the values passed,\
            negative or zero values
        """
        
        with self.assertRaises(ValueError) as context:
            rect6 = Rectangle(0, 1)
        self.assertEqual("width must be > 0", str(context.exception))
        with self.assertRaises(ValueError) as context:
            rect6 = Rectangle(-1, 1)
        self.assertEqual("width must be > 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            rect6 = Rectangle(1, 0)
        self.assertEqual("height must be > 0", str(context.exception))
        with self.assertRaises(ValueError) as context:
            rect6 = Rectangle(1, -1)
        self.assertEqual("height must be > 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            rect6 = Rectangle(1, 2, -3, 4, 5)
        self.assertEqual("x must be >= 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            rect6 = Rectangle(1, 2, 3, -4, 5)
        self.assertEqual("y must be >= 0", str(context.exception))

    def test_rectangle_area(self):
        """Check the area of a rectangle"""

        self.assertEqual(Rectangle(1, 2).area(), 1 * 2)
        self.assertEqual(Rectangle(11, 22).area(), 11 * 22)
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).area(), 1 * 2)
        self.assertEqual(Rectangle(187, 8756, 38, 48, 58).area(), 187 * 8756)

    def test_rectangle_display_with_custom_stream(self):
        """Check the rectangle printed to stdout"""

        rect7 = Rectangle(4, 3, 2, 2, 1)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rect7.display()
            printed_result = mock_stdout.getvalue()
        expected_result = "\n\n  ####\n  ####\n  ####\n" 

        self.assertEqual(printed_result, expected_result)

    def test_string_represantation_of_rect(self):
        """Checks the string represantion of rectangle class"""
        rect8 = Rectangle(10, 20, 30, 40, 50)

        str_repr = str(rect8)
        expected_result = "[Rectangle] (50) 30/40 - 10/20"
        self.assertEqual(str_repr, expected_result)

    def test_rectangle_update_with_args(self):
        """Check if succesfully unpacked and asigned the args to respective attributes"""

        rect9 = Rectangle(10, 20, 30, 40)

        rect9.update(89)
        self.assertEqual(rect9.id, 89)

        rect9.update(1, 2)
        self.assertEqual(2, rect9.width)

        rect9.update(1, 2, 3)
        self.assertEqual(3, rect9.height)

        rect9.update(1, 2, 3, 4)
        self.assertEqual(4, rect9.x)

        rect9.update(1, 2, 3, 4, 5)
        self.assertEqual(5, rect9.y)

        rect9.update(1, 2, 3, 4, 5)
        self.assertEqual(str(rect9), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_update_with_wrong_type_args(self):
        """Check the args if correctly validated"""

        rect = Rectangle(10, 20, 30, 40)

        with self.assertRaises(TypeError) as context:
            rect.update(1, "one")
        self.assertEqual("width must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect.update(1, 3, 4, "one")
        self.assertEqual("x must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect.update(1, 3, 5, 6, "one")
        self.assertEqual("y must be an integer", str(context.exception))

    def test_update_with_args_and_kwargs(self):
        """Check if succssfully unpacked the kwargs"""

        rect = Rectangle(10, 20, 30, 40)

        rect.update(id=10)
        self.assertEqual(10, rect.id)

        rect.update(x=3, id=10)
        self.assertEqual(3, rect.x)

        rect.update(y=22, x=3)
        self.assertEqual(22, rect.y)

        rect.update(id=10, x=3, y=22, height=5, width=8)
        self.assertEqual(8, rect.width)
        self.assertEqual(5, rect.height)

    def test_update_with_wrong_type_args_and_kwargs(self):
        """Check if attributes correctly validated"""

        rect = Rectangle(10, 20, 30, 40)

        with self.assertRaises(TypeError) as context:
            rect.update(id=2, width="one")
        self.assertEqual("width must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect.update(id=2, width=6, x="nine")
        self.assertEqual("x must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect.update(id=2, width=7, y="ten", height=11)
        self.assertEqual("y must be an integer", str(context.exception))

    def test_rectangle_to_dictionary(self):
        """Check rectangle dictionary represantion"""

        rect = Rectangle(10, 20, 30, 40)
        self.assertEqual("[Rectangle] (1) 30/40 - 10/20", str(rect))

        rect_dict = rect.to_dictionary()
        self.assertEqual("{'id': 1, 'width': 10, 'height': 20, 'x': 30, 'y': 40}", str(rect_dict))
        self.assertEqual(type(rect_dict), dict)
        self.assertEqual(rect_dict["x"], rect.x)
        self.assertEqual(rect_dict["id"], rect.id)

    def test_rectangle_to_dictionary_upacking(self):
        """Lets unpack the dictionary to update a Rectangle object"""

        rect = Rectangle(10, 20, 30, 40)
        rect_dict = rect.to_dictionary()

        rect1 = Rectangle(99, 88)
        rect1.update(**rect_dict)

        self.assertEqual(rect1.x, rect.x)
        self.assertEqual(rect1.width, 10)

        rect1.update(width=12, height=12)
        self.assertEqual(144, rect1.area())


if __name__ == '__main__':
    unittest.main()
        