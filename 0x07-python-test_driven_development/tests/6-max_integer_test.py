#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class that tests the max_integer module
    """
    def test_emptylist(self):
        """Tests the case if the list is empty.
        """
        maxint = max_integer([])
        self.assertEqual(maxint, None)

    def test_stringsinlist(self):
        """Tests the case if the list has strings.
        """
        maxint = max_integer(["Hi", "Hey", "Hello"])
        self.assertEqual(maxint, "Hi")

    def test_onestringasinput(self):
        """Tests the case if only a string is given
        to function.
        """
        maxint = max_integer("HELLO")
        self.assertEqual(maxint, 'O')

    def test_floatnumberinlist(self):
        """Tests if the list has a floatnumber
        """
        maxint = max_integer([1, -4, 5, 15.8])
        self.assertEqual(maxint, 15.8)

    def test_allfloatlist(self):
        """Tests an all float list
        """
        maxint = max_integer([1.4, -5.5, 23.6])
        self.assertEqual(maxint, 23.6)

    def test_stringinintlist(self):
        """Tests if the list has a string among ints & floats
        """
        self.assertRaises(TypeError, max_integer, [1, 5.4, "HI", [3, 2, 5]])

    def test_singleelementlist(self):
        """Tests if the list has a single element.
        """
        maxint = max_integer([30])
        self.assertEqual(maxint, 30)

    def test_tupleasinput(self):
        """Tests a tuple as input
        """
        maxint = max_integer((5, 4, -4, 45.7))
        self.assertEqual(maxint, 45.7)

    def test_dictasinput(self):
        """Tests a dict as input
        """
        a = {'a': 1, 2: 4.3, 3: 'Hi', 'Hey': 3}
        self.assertRaises(KeyError, max_integer, a)

    def test_emptystring(self):
        """Tests an empty string as input
        """
        maxint = max_integer("")
        self.assertEqual(maxint, None)


if __name__ == '__main__':
    unittest.main()
