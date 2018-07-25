# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-06-07
#
# Description: My solution to the below exercise posed by Eric Appelt
#
# Exercise: Write a program to take an integer that the user inputs and print
# the corresponding Fibonacci Number. The Fibonacci sequence begins 1, 1, 2, 3,
# 5, 8, 13, so if the user inputs 7, the user should see the 7th Fibonacci
# number printed, which is 13. If the user inputs a negative number the
# program should print an error message.

if __name__ == '__main__':
    # Get user input
    user_input = input(
        "Enter in a positive integer 'n' such that the 'nth' Fibonacci Number "
        "will be printed: ")
    fib_num = int(user_input)

    # Print error if number is not positive
    if fib_num < 0:
        print("Value is not positive. Exiting.")
        exit(-1)
    elif fib_num == 0:
        print("The Fibonacci Number in the 0 position is: 0")
    else:
        # Set the two previous Fibonacci Numbers.
        f1 = 0
        f2 = 0

        # Set the current Fibonacci Number to print.
        cur = 1

        # Get the user choice.
        while fib_num > 1:
            f1 = f2
            f2 = cur
            cur = f1 + f2
            fib_num = fib_num - 1

        print(
            "The Fibonacci Number in the '" + user_input + "' position is: "
            + str(cur))
