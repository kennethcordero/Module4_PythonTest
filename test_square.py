import math
import unittest

def test_sqrt():
    num=9
    assert math.sqrt(num) == 3

def test_square():
    num=7
    assert 7*7 == 49

def test_check():
    x = 100
    assert x >= 40