import pytest
import os
import sys
import pytest

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.fizzbuzz import fizzbuzz

def test_1():
    value = fizzbuzz(1)
    assert value == 1
