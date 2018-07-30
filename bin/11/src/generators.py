# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-30
#
# Description: Solution to the following exercises by Eric Appelt:
#
# Exercises:
# Write a generator function that returns the next X Tuesdays as
# datetime.datetime objects for midnight on that Tuesday.
# Use this to find out how many Tuesdays there are in 2025.
#
# Make a similar “infinite generator” that endlessly returns Tuesdays.
# Use this infinite generator to determine the date of the last Tuesday in 2056
#
# Write a generator expression that returns the square root of the first 10M
# even integers.
# Use this in a for loop with enumerate to find the integer for which the sum
# of all previous square roots is at least 10000
# Try this again using a list comprehension rather than a generator expression
# and note the difference in performance. Explain why the generator
# expression version is so much faster.

# Libaries
import datetime
import math

# Constants
EVEN_INTS = 10000000 # Number of even integers to generate the square roots of

def generate_tuesdays(n):
    """
    Generator to return the next n Tuesdays.

    :param n: Number of Tuesdays to return.
    :return: Datetime object with time as midnight.
    """
    # Start with yesterday because date is incremented each time object is
    # generated to prevent the same day from being returned continuously
    date = datetime.date.today() - datetime.timedelta(days=1)
    for _ in range(n):
        # Add one date to prevent same date from being returned continuously.
        date = date + datetime.timedelta(days=1)
        # Keep incrementing day until it is Tuesday
        while date.isoweekday() != 2:
            date = date + datetime.timedelta(days=1)
        # Convert to datetime object with time as midnight
        yield datetime.datetime.combine(date, datetime.time.min)

def infinite_generate_tuedays():
    """
    Infinite generator that continually returns the next Tuesday.

    :return: Datetime object with time as midnight.
    """
    # Start with yesterday because date is incremented each time object is
    # generated to prevent the same day from being returned continuously
    date = datetime.date.today() - datetime.timedelta(days=1)
    while True:
        date = date + datetime.timedelta(days=1)
        # Keep incrementing day until it is Tuesday
        while date.isoweekday() != 2:
            date = date + datetime.timedelta(days=1)
        # Convert to datetime object with time as midnight
        yield datetime.datetime.combine(date, datetime.time.min)

def generate_square_roots():
    """
    Generate the square roots of the first 10 million even integers.

    :return: Square root of next even integer
    """
    val = -2 # Start with -2 since first increment will result in 0
    for _ in range(EVEN_INTS):
        val += 2
        yield math.sqrt(val)

if __name__ == '__main__':
    # Find out how many Tuesdays are in 2025
    tuesdays_list = list(generate_tuesdays(600))
    count = 0
    for tuesday in tuesdays_list:
        if tuesday.year == 2025:
            count += 1
    print("There are {} Tuesdays in the year 2025.".format(count))
    print()

    # Find the last Tuesday in 2056. Start by creating generator and getting
    # first two Tuesdays.
    generator = infinite_generate_tuedays()
    tuesday_1 = next(generator)
    tuesday_2 = next(generator)
    # Throw exception if the first Tuesday is after 2056
    if tuesday_1.year > 2056:
        raise ValueError("The next Tuesday is after 2056.")

    # Keep incrementing Tuesdays until 2057 is reached, and print out the
    # Tuesday before that
    while tuesday_2.year < 2057:
        tuesday_1, tuesday_2 = tuesday_2, next(generator)

    # Print out the last Tuesday in 2056
    print("The last Tuesday in 2056 is {}-{}".format(tuesday_1.month,
                                                     tuesday_1.day))
    print()

    # Time and compare generator function getting integer for which sum of
    # square roots of previous integers is at least 10000 to a list
    # comprehension
    start_time = datetime.time # Time generator function
    val = 0
    sum = 0

