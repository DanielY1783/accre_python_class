# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-26
#
# Description: Tests for DiceSet object for part 4 of the following exercise by
# Eric Appelt:
#
# Exercise: Add some functionality to our DiceSet class:
# 1. Implement the count_attempts method that we skipped in class
# 2. Implement maximum and minimum methods that return the max and min
# possible roll from the set
# 3. Implement a range method that returns a list of all possible values
# rolled by the set. Use this to improve count_attempts to raise an exception
#  immediately if the value is impossible
# 4. Write unit tests for the DiceSet class using pytest.

# Imports
from src.dice_set import DiceSet as DiceSet
import pytest

# Tests for __init__
def test_init_1():
    with pytest.raises(TypeError):
        d1 = DiceSet()

def test_init_2():
    d1 = DiceSet(4, 6)
    assert d1.number == 4

def test_init_3():
    d1 = DiceSet(4, 6)
    assert d1.sides == 6

def test_init_4():
    d1 = DiceSet(4, 6)
    assert d1.base == 1

def test_init_5():
    d1 = DiceSet(4, 6, 4)
    assert d1.base == 4

def test_init_6():
    with pytest.raises(TypeError):
        d1 = DiceSet(14, 6, 4, 0)

# Tests for __str__ and __repr__
def test_str_1():
    d1 = DiceSet(4, 3, 11)
    assert str(d1) == "DiceSet of 4 dice with 3 sides, base numbering 11"

def test_str_2():
    d1 = DiceSet(4, 3)
    assert str(d1) == "DiceSet of 4 dice with 3 sides, base numbering 1"

def test_repr_1():
    d1 = DiceSet(4, 3)
    assert repr(d1) == "dice.DiceSet(4, 3, 1)"

def test_repr_2():
    d1 = DiceSet(4, 3, 11)
    assert repr(d1) == "dice.DiceSet(4, 3, 11)"

# Tests for min and max
def test_max_1():
    d1 = DiceSet(4, 3)
    assert d1.max() == 12

def test_max_2():
    d1 = DiceSet(4, 3, 11)
    assert d1.max() == 132

def test_max_3():
    d1 = DiceSet(0, 3, 11)
    assert d1.max() == 0

def test_min_1():
    d1 = DiceSet(4, 3)
    assert d1.min() == 4

def test_min_2():
    d1 = DiceSet(4, 3, 11)
    assert d1.min() == 44

def test_min_3():
    d1 = DiceSet(0, 3, 11)
    assert d1.min() == 0

def test_min_4():
    d1 = DiceSet(4, 8)
    assert d1.min() == 4

# Tests for range
def test_range_1():
    d1 = DiceSet(4, 3)
    assert d1.range() == [4, 5, 6, 7, 8, 9, 10, 11, 12]

def test_range_2():
    d1 = DiceSet(2, 3, 2)
    assert d1.range() == [4, 6, 8, 10, 12]

# Test for count_attempts
def test_count_attempts_1():
    df = DiceSet(4, 3)
    with pytest.raises(ValueError):
        df.count_attempts(13)

def test_count_attempts_2():
    df = DiceSet(4, 3)
    with pytest.raises(ValueError):
        df.count_attempts(3)

def test_count_attempts_3():
    df = DiceSet(4, 3, 2)
    with pytest.raises(ValueError):
        df.count_attempts(11)
