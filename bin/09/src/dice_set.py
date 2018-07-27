# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-26
#
# Description: DiceSet object represents a set of dice. Original code by Eric
# Appelt from his Python class. Added code is to solve the following exercise
# by Eric Appelt (note that the tests for part 4 are in
# ../test/test_dice_set.py).
#
# Exercise: Add some functionality to our DiceSet class:
# 1. Implement the count_attempts method that we skipped in class
# 2. Implement maximum and minimum methods that return the max and min
# possible roll from the set
# 3. Implement a range method that returns a list of all possible values
# rolled by the set. Use this to improve count_attempts to raise an exception
#  immediately if the value is impossible
# 4. Write unit tests for the DiceSet class using pytest.


# Libaries
import random

##############################################################################
# Begin original code by Eric Appelt                                         #
##############################################################################
class DiceSet:

    def __init__(self, number, sides, base=1):
        """Set the number, sides, and bases of the DiceSet"""
        self.number = number
        self.sides = sides
        self.base = base

    def __repr__(self):
        return "dice.DiceSet({}, {}, {})".format(self.number, self.sides,
                                                 self.base)

    def __str__(self):
        return "DiceSet of {} dice with {} sides, base numbering {}".format(
            self.number, self.sides, self.base)

    def roll(self):
        """Roll the dice set and return the result"""
        total = 0
        for _ in range(self.number):
            total += random.randint(1, self.sides) * self.base
        return total

    def roll_many(self, times):
        """Roll the dice set multiple times and return the total"""
        total = 0
        for _ in range(times):
            total += self.roll()
        return total
##############################################################################
#  End original code by Eric Appelt                                          #
##############################################################################


##############################################################################
#  Begin new code by Daniel Yan                                              #
##############################################################################
    def count_attempts(self, value):
        """
        Count number of times the DiceSet is rolled before it obtains a
        certain value passed as a parameter.

        :param value: Number to roll.
        :return: Number of attempts before value is attained from a roll.
        """
        # Check that value is possible.
        if value not in self.range():
            raise ValueError("Not possible to roll {}".format(value))

        if value % self.base != 0:
            raise ValueError("Not possible to roll {}".format(value))

        attempts = 0  # Initialize DiceSet with no attempts
        # Keep rolling until value is attained, and return number of attempts.
        while True:
            roll_value = self.roll()
            attempts += 1
            if roll_value == value:
                return attempts

    def max(self):
        """
        Return maximum possible roll for the DiceSet object.

        :return: Integer value for maximum possible roll.
        """
        return self.number * self.sides * self.base

    def min(self):
        """
        Return minimum possible roll for the DiceSet object.

        :return: Integer value for minimum possible roll.
        """
        return self.number * self.base

    def range(self):
        """
        Return list containing range of possible roll values.

        :return: List containing range of possible roll values.
        """
        return list(range(self.min(), self.max() + 1, self.base))