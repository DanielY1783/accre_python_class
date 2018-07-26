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
def test_dice_set_init_1():
    with pytest.raises(TypeError):
        d1 = DiceSet()