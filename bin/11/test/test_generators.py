# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-31
#
# Description: Tests for generators.py

# Import libraries
from src import generators
import pytest
import math

# Test for generator for n Tuesdays
def test_generate_n_tuesdays_1():
    gen1 = generators.generate_tuesdays(10)
    with pytest.raises(StopIteration):
        for _ in range(11):
            next_tuesday = next(gen1)

# Test for infinite Tuesday generator
def test_generate_infinite_tuesdays_1():
    gen1 = generators.infinite_generate_tuedays()
    with pytest.raises(OverflowError):
        tuesdays_list = []
        for i in gen1:
            tuesdays_list.append(i)
