import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(0,add(""))

    def test_single_number_returns_its_value(self):
        self.assertEqual(1,add("1"))
    
    def test_two_numbers_comma_delimited_returns_sum(self):
        self.assertEqual(3,add("1,2"))

    def test_newlines_between_numbers(self):
        self.assertEqual(6,add("1\n2,3"))

    def test_custom_delimiter(self):
        self.assertEqual(3,add("//;\n1;2"))
    
    def test_negative_number_throws_exception(self):
        with self.assertRaises(ValueError):
            add("-1,2")
