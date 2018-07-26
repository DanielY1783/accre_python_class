# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-26
#
# Description: Unit tests for the below exercise posed by Eric Appelt (file
# to test is in ../../bin/08):
#
# Exercise: Do some Test-Driven Development (TDD):
#
# Define a function that takes a positive integer and returns the double
# factorial. The double factorial is defined differently for even and odd
# numbers. For example, 9!! = 9 * 7 * 5 * 3 * 1 and 6!! = 6 * 4 * 2. * The
# double factorial of zero is 0!! = 1. Don’t actually implement the function,
# just define it in a module and add a nice docstring. Otherwise leave the
# function body blank.
#
# Now write some unit tests for the function that you haven’t implemented
# yet. These tests should check that the function returns the right value for
# 0, 1, 2, and a larger even and odd number. They should also make sure that
# a ValueError is raised for a negative number. Run the tests, which should
# all fail.
#
# Implement the function body to return the correct double factorial. When
# you think you have done this correctly, run the test to ensure the
# validity of your implementation.

# Import module and pytest
from src.double_factorial import double_factorial as df
import pytest

def test_double_factorial_1():
    assert df(0) == 1

def test_double_factorial_2():
    assert df(1) == 1

def test_double_factorial_3():
    assert df(2) == 2

def test_double_factorial_4():
    assert df(6) == 48

def test_double_factorial_5():
    assert df(9) == 945

def test_double_factorial_6():
    with pytest.raises(ValueError):
        df(-1)