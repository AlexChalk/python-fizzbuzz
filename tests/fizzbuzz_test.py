import pytest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.fizzbuzz import *

def test_returns_self():
    value = fizzbuzz(1)
    assert value == 1

def test_returns_fizz():
    value = fizzbuzz(3)
    assert value == "fizz" 

def test_returns_buzz():
    value = fizzbuzz(5)
    assert value == "buzz" 

def test_returns_fizzbuzz():
    value = fizzbuzz(15)
    assert value == "Fizzbuzz" 

def test_fizzbuzz_loop():
    expected_array = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'Fizzbuzz', 16, 17, 'fizz', 19, 'buzz', 'fizz', 22, 23, 'fizz', 'buzz', 26, 'fizz', 28, 29, 'Fizzbuzz']
    assert fizzbuzz_loop() == expected_array

