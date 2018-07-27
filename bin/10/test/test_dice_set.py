# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-27
#
# Description: Tests for WeightedDiceSet and TrackingDiceSet


# Imports
from src.dice_set import DiceSet as DiceSet
from src.dice_set import WeightedDiceSet as WeightedDiceSet
import pytest

# Tests for WeightedDiceSet __init__
def test_weighted_dice_set_init_1():
    wds = WeightedDiceSet(4, 3)
    assert wds.weights == [1, 1, 1]

def test_weighted_dice_set_init_2():
    wds = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    assert wds.weights == [1, 3, 2]

# Tests for WeightedDiceSet __add__ and __radd__
def test_weighted_dice_set_add_1():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    wds2 = WeightedDiceSet(2, 3, weights=[3, 3, 1])
    wds3 = wds1 + wds2
    assert wds3.number == 6

def test_weighted_dice_set_add_2():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    wds2 = WeightedDiceSet(2, 3, weights=[3, 3, 1])
    wds3 = wds1 + wds2
    assert wds3.weights == [4, 6, 3]