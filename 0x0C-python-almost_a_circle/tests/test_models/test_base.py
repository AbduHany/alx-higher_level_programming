#!/usr/bin/python3
"""This module contains all unittests for the ``Base`` class
"""
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import json
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
    Testing is done and compared to the standard json.dumps method.
    """
    def test_rec_dictlist(self):
        rec1 = Rectangle(1, 4, 5, 0, 1)
        rec2 = Rectangle(5, 5, 6, 1, 0)
        dictlist = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_square_dictlist(self):
        squ1 = Square(4, 5, 0, 1)
        squ2 = Square(5, 5, 6)
        dictlist = [squ1.to_dictionary(), squ2.to_dictionary()]
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_mixed_dictlist(self):
        squ = Square(5, 6, 0, 1)
        rec = Rectangle(2, 4, 5, 1, 0)
        dictlist = [squ.to_dictionary(), rec.to_dictionary()]
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_emptylist(self):
        dictlist = []
        self.assertEqual(Base.to_json_string(dictlist), "[]")

    def test_Nonelist(self):
        dictlist = None
        self.assertEqual(Base.to_json_string(dictlist), "[]")

    def test_no_dictlist(self):
        dictlist = [1, "Hello", 4.5]
        self.assertEqual(Base.to_json_string(dictlist), '[1, "Hello", 4.5]')

    def test_singledictarg(self):
        dictlist = dict(id=3, width=4, height=5, x=2, y=4)
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_stringarg(self):
        dictlist = "Abdu"
        self.assertEqual(Base.to_json_string(dictlist), '"Abdu"')

    def test_intarg(self):
        dictlist = 500
        with self.assertRaises(TypeError):
            Base.to_json_string(dictlist)

    def test_floatarg(self):
        dictlist = 2.3
        with self.assertRaises(TypeError):
            Base.to_json_string(dictlist)

    def test_tuplearg(self):
        dictlist = (5, 6, 7)
        self.assertEqual(Base.to_json_string(dictlist), '[5, 6, 7]')

    def test_setarg(self):
        dictlist = {1, 3, 3, 5}
        with self.assertRaises(TypeError):
            Base.to_json_string(dictlist)

    def test_listoflists(self):
        dictlist = [[dict(id=1, size=4, x=2, y=1)],
                    [dict(id=4, size=6, x=0, y=3)]]
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_emptyargs(self):
        self.assertEqual(Base.to_json_string(), 1)

    def test_morethanonearg(self):
        dictlist = [dict(id=1, size=5, x=2, y=1)]
        dictlist2 = [dict(id=3, size=10, x=3, y=5)]
        self.assertEqual(Base.to_json_string(dictlist, dictlist2), 1)

class base_savetofile_test(unittest.TestCase):
    """This class tests the ``load_from_file``
    """
    def test_em(self):
        pass
