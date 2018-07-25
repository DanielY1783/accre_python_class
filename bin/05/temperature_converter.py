# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-25
#
# Description: My solution to the below exercise posed by Eric Appelt
#
# Exercise: Write a new temperature converter program written entirely in
# functions, that simply calls a main() function to run the interactive loop,
# with the following constraints:
#
# There should be a function that takes a string of the form 23.4 K,
# determines if it is Kelvin, Celsius, or Fahrenheit, and returns a 3-tuple
# of numbers representing the temperature in C/K/F. An invalid string should
# raise an exception.
#
# There should be a function that takes the 3-tuple of numbers representing
# C/K/F and prints a nicely formatted output of the temperatures to the screen
#
# The main loop should prompt the user to input temperatures or quit and run
# a loop. The menu/prompt string should be a global constant.

# Constants
MENU_STRING = """Enter a temperature in Kelvin, Celsius, or Fahrenheit in the 
form "23.4 K". Enter "q" to quit: """


def convert_string(input_string):
    """
    Convert a string representation of a temperature to a tuple representing
    the temperature in C, K, F

    :param input_string: String to convert. Should contain either "q"
    to exit the program immediately, or a numeric value,
    followed by a space, followed by a single letter: "C" for Celsius,
    "K" for Kelvin, or "F" for Fahrenheit. ValueError will be raised if the
    string is not in the correct format.
    :return: Tuple of numbers. First number is temperature in Celsius,
    second number is temperature in Kelvin, and third number is temperature
    in Fahrenheit.
    """
    # Check if user wants to quit
    if input_string.lower().startswith("q"):
        exit(0)

    # Split the user input.
    input_strings_list = input_string.split()

    # Check that user input is two tokens separated by whitespace
    if (len(input_strings_list) != 2):
        raise ValueError("Invalid input. Must enter number followed by space, "
                         "then a character, to specify temperature.")

    # Get temperature and which unit it is in.
    temperature_str = input_strings_list[0]
    unit = input_strings_list[1]

    # Raise exception if temperature is not numeric value.
    try:
        float(temperature_str)
    except ValueError:
        print("Invalid temperature value")

    # Raise exception if unit is not Kelvin, Celsius, or Fahrenheit.
    if not (unit.lower().startswith("k") or unit.lower().startswith(
            "c") or unit.lower().startswith("f")):
        raise ValueError("Invalid unit for temperature. Use K for Kelvin, "
                         "C for Celsius, or F for Fahrenheit")

    # Convert to tuple of numeric values in the form (C, K, F)
    temperature_float = float(temperature_str)
    if unit.lower().startswith("k"):
        return (temperature_float - 273.15, temperature_float,
                temperature_float * 9 / 5 - 459.67)
    elif unit.lower().startswith("c"):
        return (temperature_float, temperature_float + 273.15,
                temperature_float * 9 / 5 + 32)
    else:
        return ((temperature_float - 32) * 5 / 9,
                (temperature_float + 459.67) * 5 / 9, temperature_float)


def print_temps(temperatures):
    """
    Prints temperatures from tuple containing temperature in (C, K, F) form
    to standard output.
    :param temperatures: Tuple of three integers containing temperature in
    (C, K, F) form to standard output.
    :return: None
    """
    print("The temperature in Celsius is {0:.2F} C.".format(temperatures[0]))
    print("The temperature in Kelvin is {0:.2F} K.".format(temperatures[1]))
    print("The temperature in Fahrenheit is {0:.2F} F.".format(temperatures[2]))


if __name__ == '__main__':
    # Keep prompting user for input
    while True:
        user_input = input(MENU_STRING)
        temperatures = convert_string(user_input)
        print_temps(temperatures)
