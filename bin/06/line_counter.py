# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-25
#
# Description: My solution to the below exercise posed by Eric Appelt
#
# Exercise: Write a command line utility in python that counts the number
# of lines in a file and prints them. to standard output.
#
# The utility should take the name of a file as an argument. To do this use
# import sys and then sys.argv[1] will be the first argument given.
#
# By trial and error, determine the type of exception raised when the user
# fails to run the program with an argument, the file specified does not
# exist, or the user does not have permission to read the file specified.
#
# Using try/except blocks, handle each of these exception types separately
# and send an appropriate message to the user in each case.

import sys

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
        count = 0
        with open(file_name, "r") as read_file:
            for _ in read_file:
                count += 1
        print("{} has {} line(s)".format(file_name, count))
    except IndexError:
        print("No file specified. Specify file in first command line argument")
    except FileNotFoundError:
        print("File does not exist. Make sure that directory and extension of "
              "file are included.")
    except PermissionError:
        print("You do not have permission to read the file. Please obtain "
              "read permission to file and try again.")