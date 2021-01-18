import pytest
from Task import Window

def test_linear_func(): # x + 3 Range(1 - 10)
    obj = Window()
    assert  obj.result == [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
