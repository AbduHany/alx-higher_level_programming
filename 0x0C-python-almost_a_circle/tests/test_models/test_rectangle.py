#!/usr/bin/python3
"""This module contains all unittests for the ``Rectangle`` class
"""
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import json
import unittest
import os
import sys
import io


class rec_init_test(unittest.TestCase):
    """This method tests the init method of the base class.
    """
    def test_noarg(self):
        with self.assertRaises(TypeError):
            a = Rectangle()

    def test_singlearg(self):
        with self.assertRaises(TypeError):
            a = Rectangle(50)

    def test_2args(self):
        a = Rectangle(50, 20)
        self.assertEqual(a.width, 50)

    def test_3args(self):
        a = Rectangle(20, 30, 5)
        self.assertEqual(a.width, 20)

    def test_4args(self):
        a = Rectangle(20, 30, 5, 7)
        self.assertEqual(a.width, 20)

    def test_4args(self):
        a = Rectangle(20, 30, 5, 7, 8)
        self.assertEqual(str(a), "[Rectangle] (8) 5/7 - 20/30")

    def test_stringinargs(self):
        with self.assertRaises(TypeError):
            a = Rectangle(20, "HI", 5, 6, 8)

    def test_floatinargs(self):
        with self.assertRaises(TypeError):
            a = Rectangle(20, 40, 4.4, 5, 6)

    def test_tuplearg(self):
        with self.assertRaises(TypeError):
            a = Rectangle((20, 3, 4), 2, 3, 4, 5)

    def test_dictarg(self):
        with self.assertRaises(TypeError):
            a = Rectangle(40, 20, {3: 4}, 4, 5)

    def test_lastattr(self):
        a = Rectangle(40, 20, 4, 4, "FakeId")
        self.assertEqual(str(a), "[Rectangle] (FakeId) 4/4 - 40/20")

    def test_negativewidth(self):
        with self.assertRaises(ValueError):
            a = Rectangle(-40, 3, 5, 7, 3)

    def test_negativeheight(self):
        with self.assertRaises(ValueError):
            a = Rectangle(40, -3, 5, 7, 3)

    def test_negativex(self):
        with self.assertRaises(ValueError):
            a = Rectangle(40, 3, -5, 7, 3)

    def test_negativey(self):
        with self.assertRaises(ValueError):
            a = Rectangle(40, 3, 5, -7, 3)

    def test_hugenumbers(self):
        a = Rectangle(999999999999999999, 9999999999999999,
                      999999999999999999, 9999999999999999,
                      999999999999999999)
        self.assertEqual(str(a), "[Rectangle] (999999999999999999) "
                         "999999999999999999/9999999999999999 - "
                         "999999999999999999/9999999999999999")


class rec_areamethod_test(unittest.TestCase):
    """This class tests the area method of the Rectangle
    class
    """
    def test_rectarea(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        self.assertEqual(rec.area(), 20)

    def test_squarearea(self):
        squ = Square(5, 0, 1, 4)
        self.assertEqual(squ.area(), 25)

    def test_givenarg(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        with self.assertRaises(TypeError):
            rec.area("Hello")


class rec_settergetter_test(unittest.TestCase):
    """This class tests the various setter and getter
    methods of the attributes
    """
    def test_widthsetter(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        rec.width = 10
        self.assertEqual(rec.width, 10)

    def test_heightsetter(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        rec.height = 10
        self.assertEqual(rec.height, 10)

    def test_xsetter(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        rec.x = 10
        self.assertEqual(rec.x, 10)

    def test_ysetter(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        rec.y = 10
        self.assertEqual(rec.y, 10)

    def test_invalidtype(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        with self.assertRaises(TypeError):
            rec.width = "HELLO"

    def test_invalidvalue(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        with self.assertRaises(ValueError):
            rec.width = -100


class rec_display_test(unittest.TestCase):
    """This class tests the display instance method.
    """
    def setUp(self):
        """redirecting stdout to output
        """
        self.output = io.StringIO()
        self.originalstdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """resetting stdout to its original
        value
        """
        sys.stdout = self.originalstdout

    def test_rectangle(self):
        rec = Rectangle(2, 3, 0, 0, 2)
        rec.display()
        self.assertEqual(self.output.getvalue(), "##\n##\n##\n")

    def test_square(self):
        s = Square(5, 0, 0)
        s.display()
        self.assertEqual(self.output.getvalue(), "#####\n#####\n#####\n"
                         "#####\n#####\n")
