import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(0,add(""))

    def test_single_number_returns_its_value(self):
        self.assertEqual(1,add("1"))
    
    def test_two_numbers_comma_delimited_returns_sum(self):
        self.assertEqual(3,add("1,2"))