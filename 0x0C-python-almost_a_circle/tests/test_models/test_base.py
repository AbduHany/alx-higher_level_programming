#!/usr/bin/python3
"""This module contains all unittests for the ``Base`` class
"""
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import unittest


class base_init_test(unittest.TestCase):
    """This method tests the init method of the base class.
    """
    def test_noarg(self):
        a = Base()
        b = Base()
        self.assertEqual(b.id, a.id + 1)

    def test_singlearg(self):
        a = Base(50)
        self.assertEqual(a.id, 50)

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            a = Base(50, 1)

    def test_strinit(self):
        a = Base("Hello")
        self.assertEqual(a.id, "Hello")

    def test_strfloat(self):
        a = Base(5.4)
        self.assertEqual(a.id, 5.4)

    def test_listarg(self):
        a = Base([1, 2, 3])
        self.assertEqual(a.id, [1, 2, 3])

    def test_dictarg(self):
        a = Base({1: 2, 2: 3})
        self.assertEqual(a.id, {1: 2, 2: 3})

    def test_none(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)

    def test_NaN(self):
        num = float('nan')
        a = Base(num)
        self.assertNotEqual(a.id, num)

    def test_inf(self):
        num = float('inf')
        a = Base(num)
        self.assertEqual(a.id, num)

    def test_changeid(self):
        a = Base(50)
        a.id = 20
        self.assertEqual(a.id, 20)

    def test_accessprivattr(self):
        a = Base(None)
        with self.assertRaises(AttributeError):
            id = a.__nb_instances

    def test_bool(self):
        a = Base(True)
        self.assertTrue(a.id)
        b = Base(False)
        self.assertFalse(b.id)


    def test_tuple(self):
        a = Base((1, 2, 3))
        self.assertEqual(a.id, (1, 2, 3))

    def test_set(self):
        a = Base({1, 2, 3})
        self.assertEqual(a.id, {1, 2, 3})

class base_tojsonstring_test(unittest.TestCase):
    """This method tests the ``to_json_string`` method of the base class.
    """
    
