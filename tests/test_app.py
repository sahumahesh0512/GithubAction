# tests/test_app.py

import unittest
from app import my_function

class TestMyFunction(unittest.TestCase):
    def test_my_function(self):
        # Test case 1: Ensure the function returns the expected result
        result = my_function(3, 4)
        self.assertEqual(result, 7)

        # Test case 2: Ensure the function works with negative numbers
        result = my_function(-3, 4)
        self.assertEqual(result, 1)

        # Test case 3: Ensure the function works with zero
        result = my_function(0, 4)
        self.assertEqual(result, 4)

    

