import pytest
from app import my_function

def test_my_function():
    # Test case 1: Ensure the function returns the expected result
    result = my_function(3, 4)
    assert result == 7

    # Test case 2: Ensure the function works with negative numbers
    result = my_function(-3, 4)
    assert result == 1

    # Test case 3: Ensure the function works with zero
    result = my_function(0, 4)
    assert result == 4


