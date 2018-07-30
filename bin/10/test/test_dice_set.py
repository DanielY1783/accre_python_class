# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-27
#
# Description: Tests for WeightedDiceSet and TrackingDiceSet


# Imports
from src.dice_set import DiceSet as DiceSet
from src.dice_set import WeightedDiceSet as WeightedDiceSet
from src.dice_set import TrackingDiceSet as TrackingDiceSet
import pytest


# Tests for WeightedDiceSet __init__
def test_weighted_dice_set_init_1():
    wds = WeightedDiceSet(4, 3)
    assert wds.weights == [1, 1, 1]


def test_weighted_dice_set_init_2():
    wds = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    assert wds.weights == [1, 3, 2]


# Tests for WeightedDiceSet __add__
# Start with adding two WeightedDiceSets
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

# Test adding a WeightedDiceSet and a DiceSet
def test_weighted_dice_set_add_3():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    ds2 = DiceSet(3, 3)
    wds3 = wds1 + ds2
    assert wds3.number == 7

def test_weighted_dice_set_add_4():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    ds2 = DiceSet(3, 3)
    wds3 = wds1 + ds2
    assert wds3.weights == [2, 4, 3]

# Tests to see that adding an invalid object raises an exception
def test_weighted_dice_set_add_5():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    wds2 = WeightedDiceSet(2, 3, base=2, weights=[3, 3, 1])
    with pytest.raises(TypeError):
        wds3 = wds1 + wds2

def test_weighted_dice_set_add_6():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    wds2 = WeightedDiceSet(2, 2, weights=[3, 3, 1])
    with pytest.raises(TypeError):
        wds3 = wds1 + wds2

def test_weighted_dice_set_add_7():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    with pytest.raises(TypeError):
        wds3 = wds1 + 4


# Repeat WeightedDiceSet tests for __radd__
# Test adding a WeightedDiceSet and a DiceSet
def test_weighted_dice_set_add_8():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    ds2 = DiceSet(3, 3)
    wds3 = ds2 + wds1
    assert wds3.number == 7

def test_weighted_dice_set_add_9():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    ds2 = DiceSet(3, 3)
    wds3 = ds2 + wds1
    assert wds3.weights == [2, 4, 3]

# Tests to see that adding an invalid object raises an exception
def test_weighted_dice_set_add_10():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    ds2 = DiceSet(3, 4)
    with pytest.raises(TypeError):
        wds3 = ds2 + wds1

def test_weighted_dice_set_add_11():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    ds2 = DiceSet(3, 4, base=2)
    with pytest.raises(TypeError):
        wds3 = ds2 + wds1

def test_weighted_dice_set_add_12():
    wds1 = WeightedDiceSet(4, 3, weights=[1, 3, 2])
    with pytest.raises(TypeError):
        wds3 = 4 + wds1

# Tests for TrackingDiceSet roll history
def test_tracking_dice_set_1():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    assert roll_1 == tds1._roll_history[0]

def test_tracking_dice_set_2():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    assert roll_2 == tds1._roll_history[1]

def test_tracking_dice_set_3():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    assert roll_3 == tds1._roll_history[2]

# Tests for TrackingDiceSet get_state
def test_tracking_dice_set_4():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    assert tds1.get_state(0) == (4, 3, 1)

def test_tracking_dice_set_5():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    assert tds1.get_state(2) == (4, 3, 1)

def test_tracking_dice_set_6():
    tds1 = TrackingDiceSet(4, 3)
    tds1.number = 2
    roll_1 = tds1.roll()
    tds1.number = 3
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    tds1.base = 5
    assert tds1.get_state(0) == (2, 3, 1)

def test_tracking_dice_set_7():
    tds1 = TrackingDiceSet(4, 3)
    tds1.number = 2
    roll_1 = tds1.roll()
    tds1.number = 3
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    tds1.base = 5
    assert tds1.get_state(1) == (3, 3, 1)

def test_tracking_dice_set_8():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    tds1.sides = 4
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    roll_4 = tds1.roll()
    tds1.sides = 5
    tds1.base = 2
    roll_5 = tds1.roll()
    tds1.sides = 6
    roll_6 = tds1.roll()
    assert tds1.get_state(0) == (4, 3, 1)

def test_tracking_dice_set_9():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    tds1.sides = 4
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    roll_4 = tds1.roll()
    tds1.sides = 5
    tds1.base = 2
    roll_5 = tds1.roll()
    tds1.sides = 6
    roll_6 = tds1.roll()
    assert tds1.get_state(1) == (4, 4, 1)

def test_tracking_dice_set_10():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    tds1.sides = 4
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    roll_4 = tds1.roll()
    tds1.sides = 5
    tds1.base = 2
    roll_5 = tds1.roll()
    tds1.sides = 6
    roll_6 = tds1.roll()
    assert tds1.get_state(2) == (4, 4, 1)

def test_tracking_dice_set_11():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    tds1.sides = 4
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    roll_4 = tds1.roll()
    tds1.sides = 5
    tds1.base = 2
    roll_5 = tds1.roll()
    tds1.sides = 6
    roll_6 = tds1.roll()
    assert tds1.get_state(3) == (4, 4, 1)

def test_tracking_dice_set_12():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    tds1.sides = 4
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    roll_4 = tds1.roll()
    tds1.sides = 5
    tds1.base = 2
    roll_5 = tds1.roll()
    tds1.sides = 6
    roll_6 = tds1.roll()
    assert tds1.get_state(4) == (4, 5, 2)

def test_tracking_dice_set_13():
    tds1 = TrackingDiceSet(4, 3)
    roll_1 = tds1.roll()
    tds1.sides = 4
    roll_2 = tds1.roll()
    roll_3 = tds1.roll()
    roll_4 = tds1.roll()
    tds1.sides = 5
    tds1.base = 2
    roll_5 = tds1.roll()
    tds1.sides = 6
    roll_6 = tds1.roll()
    assert tds1.get_state(5) == (4, 6, 2)