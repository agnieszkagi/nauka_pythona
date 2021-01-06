#! /usr/bin/python3

import unittest
from calculator import calculate
class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)
    def test_odejmowanie(self):
        r = calculate(10, 2, '-')
        self.assertEqual(r, 8)
    def test_mnozenie(self):
        r = calculate(5, 2, '*')
        self.assertEqual(r, 10)
    def test_dzielenie(self):
        r = calculate(20, 10, '/')
        self.assertEqual(r, 2)
    def test_potega(self):
        r = calculate(2, 2, '^')
        self.assertEqual(r, 4)
    def test_reszta_dzielenie(self):
        r = calculate(9, 2, '%')
        self.assertEqual(r, 1)
