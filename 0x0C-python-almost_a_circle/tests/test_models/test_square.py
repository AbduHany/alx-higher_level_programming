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


class squ_settergetter_test(unittest.TestCase):
    """This class tests the various setter and getter
    methods of the attributes
    """
    def test_sizesetter(self):
        s = Square(5, 4, 2, 3)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_sizesetter(self):
        s = Square(5, 4, 2, 3)
        s.size = 10
        self.assertEqual(s.width, 10)

    def test_sizesetter(self):
        s = Square(5, 4, 2, 3)
        s.size = 10
        self.assertEqual(s.height, 10)

    def test_xsetter(self):
        s = Square(5, 4, 2, 3)
        s.x = 10
        self.assertEqual(s.x, 10)

    def test_ysetter(self):
        s = Square(5, 4, 2, 3)
        s.y = 10
        self.assertEqual(s.y, 10)

    def test_invalidtype(self):
        s = Square(5, 4, 2, 3)
        with self.assertRaises(TypeError):
            s.size = "HELLO"

    def test_invalidvalue(self):
        s = Square(5, 4, 2, 3)
        with self.assertRaises(ValueError):
            s.size = -100


class squ_str_test(unittest.TestCase):
    """This class tests the str representation of a
    square or square inherited class object.
    """
    def test_square(self):
        s = Square(3, 2, 0, 2)
        self.assertEqual(str(s), "[Square] (2) 2/0 - 3")

    def test_args(self):
        s = Square(3, 2, 0, 2)
        with self.assertRaises(TypeError):
            s.__str__("HI")


class squ_update_test(unittest.TestCase):
    """This class tests the update instance method for
    a square or a square inherited class object.
    """
    def test_updatelist(self):
        s = Square(5, 4, 0, 0)
        newattr = [1, 2, 3, 4]
        s.update(*newattr)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_updaterecdict(self):
        s = Square(5, 4, 0, 0)
        newattr = dict(id=1, width=2, height=3, x=4, y=4)
        s.update(**newattr)
        self.assertEqual(str(s), "[Square] (1) 4/4 - 5")

    def test_updatedict(self):
        s = Square(5, 4, 0, 0)
        newattr = dict(id=1, size=2, x=4, y=4)
        s.update(**newattr)
        self.assertEqual(str(s), "[Square] (1) 4/4 - 2")

    def test_update_listonearg(self):
        """updates only the id if one arg is given
        """
        s = Square(5, 4, 0, 0)
        newattr = [1]
        s.update(*newattr)
        self.assertEqual(str(s), "[Square] (1) 4/0 - 5")

    def test_update_listtwoarg(self):
        """updates  the id & width if one arg is given
        """
        s = Square(10, 10, 0, 0)
        newattr = [1, 4]
        s.update(*newattr)
        self.assertEqual(str(s), "[Square] (1) 10/0 - 4")

    def test_update_listthreearg(self):
        """updates only the id, width & height if one arg is given
        """
        s = Square(10, 10, 0, 0)
        newattr = [1, 4, 5]
        s.update(*newattr)
        self.assertEqual(str(s), "[Square] (1) 5/0 - 4")

    def test_update_listfourarg(self):
        """updates only the id, width, height & x if one arg is given
        """
        s = Square(10, 10, 0, 0)
        newattr = [1, 4, 5, 6]
        s.update(*newattr)
        self.assertEqual(str(s), "[Square] (1) 5/6 - 4")

    def test_update_listfive_arg(self):
        """updates only the id, width, height, x & y if one arg is given
        """
        s = Square(10, 10, 0, 0)
        newattr = [1, 4, 5, 6, 10]
        s.update(*newattr)
        self.assertEqual(str(s), "[Square] (1) 5/6 - 4")

    def test_update_morethanfive_arg(self):
        """ignores any list item that is indexed at more than 4
        """
        s = Square(10, 10, 0, 0)
        newattr = [1, 4, 5, 6, 10, 20]
        s.update(*newattr)
        self.assertEqual(str(s), "[Square] (1) 5/6 - 4")

    def test_update_onekeydict(self):
        s = Square(10, 10, 0, 0)
        newattr = dict(id=4)
        s.update(**newattr)
        self.assertEqual(str(s), "[Square] (4) 10/0 - 10")

    def test_update_2keydict(self):
        s = Square(10, 10, 0, 0)
        newattr = dict(id=4, abdu=3)
        s.update(**newattr)
        self.assertEqual(str(s), "[Square] (4) 10/0 - 10")

    def test_update_strarg(self):
        s = Square(10, 10, 0, 0)
        s.update("Hello")
        self.assertEqual(str(s), "[Square] (Hello) 10/0 - 10")

    def test_update_intarg(self):
        s = Square(10, 10, 0, 0)
        s.update(3)
        self.assertEqual(str(s), "[Square] (3) 10/0 - 10")

    def test_update_floatarg(self):
        s = Square(10, 10, 0, 0)
        s.update(4.5)
        self.assertEqual(str(s), "[Square] (4.5) 10/0 - 10")

    def test_update_emptylist(self):
        s = Square(10, 10, 0, 0)
        s.update(*[])
        self.assertEqual(str(s), "[Square] (0) 10/0 - 10")

    def test_update_emptydict(self):
        s = Square(10, 10, 0, 0)
        s.update(**dict())
        self.assertEqual(str(s), "[Square] (0) 10/0 - 10")

    def test_update_Nonearg(self):
        s = Square(10, 10, 0, 0)
        s.update(None)
        self.assertEqual(str(s), "[Square] (None) 10/0 - 10")

    def test_update_floatinf(self):
        s = Square(10, 10, 0, 0)
        s.update(float('inf'))
        self.assertEqual(str(s), "[Square] (inf) 10/0 - 10")

    def test_update_floatnan(self):
        s = Square(10, 10, 0, 0)
        s.update(float('nan'))
        self.assertEqual(str(s), "[Square] (nan) 10/0 - 10")

    def test_update_negativeid(self):
        s = Square(10, 10, 0, 0)
        s.update([-4, 5])
        self.assertEqual(str(s), "[Square] ([-4, 5]) 10/0 - 10")

    def test_update_multipleargs(self):
        s = Square(10, 10, 0, 0)
        s.update(-4, 5, 6, 4, 3, 2)
        self.assertEqual(str(s), "[Square] (-4) 6/4 - 5")

    def test_update_negativewidth(self):
        s = Square(10, 10, 0, 0)
        attr = [4, -5, 3, 4, 5]
        with self.assertRaises(ValueError):
            s.update(*attr)

    def test_update_negativeheight(self):
        s = Square(10, 10, 0, 0)
        attr = [4, 5, -3, 4, 5]
        with self.assertRaises(ValueError):
            s.update(*attr)

    def test_update_negativex(self):
        s = Square(10, 10, 0, 0)
        attr = [4, 5, 3, -4, 5]
        with self.assertRaises(ValueError):
            s.update(*attr)

    def test_update_negativey(self):
        s = Square(10, 10, 0, 0)
        attr = [4, 5, 3, 4, -5]
        s.update(*attr)
        self.assertEqual(str(s), "[Square] (4) 3/4 - 5")


class squ_todictionary_test(unittest.TestCase):
    """Tests the todictionary instance attribute.
    """
    def test_squaretodict(self):
        s = Square(10, 10, 0, 2)
        self.assertEqual(s.to_dictionary(), dict(
            id=2, size=10, x=10, y=0
        ))

        def test_oneargument(self):
            s = Square(10, 10, 0, 1)
            with self.assertRaises(TypeError):
                mydict = s.to_dictionary("hi")
