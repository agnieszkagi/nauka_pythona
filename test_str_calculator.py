#! /usr/bin/python3

import unittest

from calculator import str_calculator

class TestStringCalculator(unittest.TestCase):

    def test_concat(self):
        r = str_calculator('a', 'c', 'concat')
        self.assertEqual(r, 'ac')

    def test_zawiera(self):
        r = str_calculator('a', 'aaa', 'incl')
        self.assertEqual(r, True)

    def test_niezawiera(self):
        r = str_calculator('b', 'aaa', 'notincl')
        self.assertEqual(r, False)

    def test_konczysie(self):
        r = str_calculator('a', 'aadadda', 'end')
        self.assertEqual(r, True)

    def test_wielkielitery(self):
        r = str_calculator('ada', 'ADA', 'upper')
        self.assertEqual(r, True)
