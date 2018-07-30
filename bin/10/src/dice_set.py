# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-27
#
# Description: DiceSet object represents a set of dice, and TrackingDiceSet
# and WeightedDiceSet are subclasses. Original code by Eric
# Appelt from his Python class. Added code is to solve the following exercises
# by Eric Appelt.
#
# Exercises:
# 1. Make a TrackingDiceSet subclass of our DiceSet class that
# keeps track of all the values that have been rolled in a list:
#
# Use super() when implementing roll() which should both return the value
# of the roll and append it to a list stored as an attribute
#
# Use @property decorators to encode changes to number, sides, and base.
# When one of these properties is changed, append a tuple encoding the
# previous value and number of rolls that have been performed so far as a
# tuple in a list
#
# Add a method to allow you to lookup the number, sides, and base that the
# DiceSet had for a particular roll in the history by index and return these
# properties as a tuple.
#
# 2. Extend the WeightedDiceSet using __add__ so that you can add two
# WeightedDiceSet classes with the resultant weights being appropriately
# averaged.
#
# Now use the isinstance built-in method to allow adding WeightedDiceSet
# to a regular DiceSet by treating the regular DiceSet as having weights of 1
# and returning a WeightedDiceSet with this averaged in.
#
# Notice what happens when you add a WeightedDiceSet to a DiceSet but
# switch the order of the objects on either side of the + operator. You can
# implement the __radd__ method of the WeightedDiceSet to do the same thing
# as __add__ (or just call it) and fix this behavior to always use __add__ as
# defined in WeightedDiceSet when the object is added to a regular DiceSet


# Libaries
import random


##############################################################################
# Begin original code by Eric Appelt                                         #
##############################################################################
class DiceSet:

    def __init__(self, number, sides, base=1):
        """
        Set the number, sides, and bases of the DiceSet
        """
        self._number = number
        self.sides = sides
        self.base = base

    @classmethod  # This is a class method decorator and refers to the class
    # rather than object
    def tds(cls):
        """
        Return a set of three six-sided dice with base 1
        """
        return cls(3, 6)

    @classmethod
    def copy(cls, other):
        return cls(other.number, other.sides, base=other.base)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    def __repr__(self):
        return "dice.DiceSet({}, {}, {})".format(self._number, self._sides,
                                                 self._base)

    def __str__(self):
        return "DiceSet of {} dice with {} sides, base numbering {}".format(
            self._number, self._sides, self._base)

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

    def __add__(self, other):
        if not isinstance(other, DiceSet):
            raise TypeError("Cannot add a DiceSet to {0}".format(type(other)))

        if self.sides != other.sides or self.base != other.base:
            raise ValueError("Cannot add DiceSets with differing sides or base")

        return DiceSet(self.number + other.number, self.sides, self.base)


class WeightedDiceSet(DiceSet):
    """A weighted DiceSet that can be more likely to roll certain values,
    as a weight is given to each side."""

    def __init__(self, number, sides, base=1, weights=None):
        """Set the number, sides, and bases of the DiceSet"""
        super().__init__(number, sides, base=base)
        if weights is not None:
            self.weights = weights
        else:
            self.weights = [1] * sides

    def roll(self):
        total = 0
        for _ in range(self.number):
            total += self._weighted_choice(self.weights) * self.base
        return total

    def _weighted_choice(self, weights):
        """Return a random list index from a list of weights by weight"""
        val = random.random() * sum(weights)
        for idx, weight in enumerate(weights):
            if val < weight:
                return idx
            val -= weight
        return len(weights) - 1

    ############################################################################
    # End   original code by Eric Appelt                                       #
    ############################################################################

    ############################################################################
    #  Begin new code by Daniel Yan                                            #
    ############################################################################

    # Start with exercise 2 and add to WeightedDiceSet
    def __add__(self, other):
        """
        Add number of dice and weights of self to other.

        :param other: DiceSet to add to. Exception will be raised if other is
        not a DiceSet, has a different number of bases, or a different number
        of sides.
        :return: New WeightedDiceSet with number and weights as the sum of
        the number and weights of self and other.
        """
        # If adding two DiceSets
        if isinstance(other, DiceSet):
            # Raise exception if number of sides for two dice is different
            if self.sides != other.sides:
                raise TypeError("Number of sides on two dice is different.")

            # Raise exception if two dice have different bases.
            if self.base != other.base:
                raise TypeError("Number of bases on two dice is different.")

            # Add weights and number if both dice are WeightedDiceSet
            if isinstance(other, WeightedDiceSet):
                new_weights = list(self.weights[i] + other.weights[i] for i in
                                   range(len(self.weights)))

                return WeightedDiceSet(number=self.number + other.number,
                                       sides=self.sides, base=self.base,
                                       weights=new_weights)

            # Use default of 1 for weights for a regular DiceSet
            else:
                new_weights = list(
                    self.weights[i] + 1 for i in range(len(self.weights)))

                return WeightedDiceSet(number=self.number + other.number,
                                       sides=self.sides, base=self.base,
                                       weights=new_weights)

        # Raise exception if adding to something that is not a DiceSet
        else:
            raise TypeError("Cannot add a WeightedDiceSet to an object that "
                            "is not a DiceSet")

    def __radd__(self, other):
        """
        Make addition commutative by calling __add__

        :param other: DiceSet to add to. Exception will be raised if other is
        not a DiceSet, has a different number of bases, or a different number
        of sides.
        :return: New WeightedDiceSet with number and weights as the sum of
        the number and weights of self and other.
        """
        return self + other