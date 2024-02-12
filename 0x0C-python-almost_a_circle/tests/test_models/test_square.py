#!/usr/bin/python3
"""This module tests the ``Square`` class
"""
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import json
import unittest
import os
import sys
import io


class squ_init_test(unittest.TestCase):
    """This method tests the init method of the square class.
    """
    def test_noarg(self):
        with self.assertRaises(TypeError):
            a = Square()

    def test_singlearg(self):
        a = Square(50)
        self.assertEqual(a.size, 50)

    def test_singlearg(self):
        a = Square(50)
        self.assertEqual(a.width, 50)

    def test_singlearg(self):
        a = Square(50)
        self.assertEqual(a.height, 50)

    def test_2args(self):
        a = Square(50, 20)
        self.assertEqual(a.x, 20)

    def test_3args(self):
        a = Square(20, 30, 5)
        self.assertEqual(a.y, 5)

    def test_4args(self):
        a = Square(20, 30, 5, 7)
        self.assertEqual(a.id, 7)

    def test_5args(self):
        with self.assertRaises(TypeError):
            a = Square(20, 30, 5, 7, 8)

    def test_stringinargs(self):
        with self.assertRaises(TypeError):
            a = Square(20, "HI", 5, 6)

    def test_floatinargs(self):
        with self.assertRaises(TypeError):
            a = Square(20, 40, 4.4, 5)

    def test_tuplearg(self):
        with self.assertRaises(TypeError):
            a = Square((20, 3, 4), 2, 3, 4)

    def test_dictarg(self):
        with self.assertRaises(TypeError):
            a = Square(40, 20, {3: 4}, 4)

    def test_lastattrstr(self):
        a = Square(40, 20, 4, "FakeId")
        self.assertEqual(str(a), "[Square] (FakeId) 20/4 - 40")

    def test_negativesize(self):
        with self.assertRaises(ValueError):
            a = Square(-40, 3, 5, 7)

    def test_negativex(self):
        with self.assertRaises(ValueError):
            a = Square(40, -3, 5, 7)

    def test_negativey(self):
        with self.assertRaises(ValueError):
            a = Square(40, 3, -5, 7)

    def test_negativeid(self):
        a = Square(40, 3, 5, -7)
        self.assertEqual(str(a), "[Square] (-7) 3/5 - 40")

    def test_hugenumbers(self):
        a = Square(999999999999999999, 9999999999999999,
                      999999999999999999, 9999999999999999)
        self.assertEqual(str(a), "[Square] (9999999999999999) 9999999999999999"
                         "/999999999999999999 - 999999999999999999")
