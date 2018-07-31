# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-31
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
import timeit

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


    # Time and generator expression getting first even integer for which sum of
    # square roots of previous even integers is at least 10000 to a list
    # comprehension
    start_time_1 = timeit.default_timer()  # Time the generator function
    first_val_1 = 0  # First value for which sum of previous is over 10000
    sum_1 = 0
    square_roots_generator = (math.sqrt(i) for i in range(0, 1000000, 2))
    # Use enumerate to keep track of values and square roots
    for val, val_root in enumerate(square_roots_generator):
        # Break if previous sum of square roots is over 10000
        if sum_1 > 10000:
            first_val_1 = 2 * val
            break
        # Add square root if sum is less than 10000
        else:
            sum_1 += val_root
    # Get elapsed time and print results
    elapsed_time_1 = timeit.default_timer() - start_time_1
    print("As computed by generator expression in {} seconds, ".format(
        elapsed_time_1))
    print("the first even integer for which the sum of the square root")
    print("of all previous even integers is greater than 10000 is {}\n".format(
        first_val_1))


    # Compare to time for list comprehension, which is slower because it
    # must allocate the entire list in memory first.
    start_time_2 = timeit.default_timer()
    square_roots_list = [math.sqrt(i) for i in range(0, 1000000, 2)]
    sum_2 = 0
    first_val_2 = 0
    for val, val_root in enumerate(square_roots_list):
        if sum_2 > 10000:
            first_val_2 = 2 * val
            break
        else:
            sum_2 += val_root
    elapsed_time_2 = timeit.default_timer() - start_time_2
    print("As computed by list comprehension in {} seconds, ".format(
        elapsed_time_2))
    print("the first even integer for which the sum of the square root")
    print("of all previous even integers is greater than 10000 is {}\n".format(
        first_val_2))