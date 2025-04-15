import unittest
from string_calculator import add

# Empty string returns zero
class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(0,add(""))