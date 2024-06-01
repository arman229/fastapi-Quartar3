# test_add.py
import pytest

def add(a, b):
    return a + b

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-3, -5) == -8

def test_add_mixed_numbers():
    assert add(3, -5) == -2
    assert add(-3, 5) == 2
