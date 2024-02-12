#!/usr/bin/python3
"""This module contains all unittests for the ``Rectangle`` class
"""
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import json
import unittest
import os


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
