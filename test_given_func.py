import pytest
from Task import Window

def test_given_func(): # 5 * x ** 3 + 2 * x Range(1 - 5)
    obj = Window()
    assert  obj.result == [7, 44, 141, 328, 635]
