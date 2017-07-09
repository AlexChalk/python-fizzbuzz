import pytest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.fizzbuzz import fizzbuzz

def test_returns_self():
    value = fizzbuzz(1)
    assert value == 1

def test_returns_fizz():
    value = fizzbuzz(3)
    assert value == "fizz" 

