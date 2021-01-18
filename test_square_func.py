import pytest
from Task import Window

def test_square_func(): # x ** 2 Range(1 - 20)
    obj = Window()
    assert  obj.result == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
