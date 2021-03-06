# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-26
#
# Description: My solution to the below exercise posed by Eric Appelt (unit
# tests are in the ../../tests folder):
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

def double_factorial(val):
    """
    Custom factorial that only multiples by odd non-negative values if passed
    odd parameter; only multiples by even non-negative values if passed even
    parameter. For example, double_factorial(5) = 5 * 3 * 1 = 15 and
    double_factorial(4) = 4 * 2 = 8. Note that double_factorial(0) = 1.

    :param val: Value to perform operation on. Must be non-negative integer.
    Exception is raised if negative.
    :return: Integer factorial of the value except that only even values will
    be multiplied if parameter is even; only odd values will be multiplied if
    parameter is odd.
    """
    if val < 0:
        raise ValueError("double_factorial must take non-negative parameter!")

    elif val == 0:
        return 1

    else:
        fact = 1
        while val > 0:
            fact = fact * val
            val -= 2
        return fact
