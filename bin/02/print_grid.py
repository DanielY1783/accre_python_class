# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-06-07
#
# Description: My solution to the below exercise posed by Eric Appelt
#
# Exercise: Do the “Character Picture Grid” project in Automate Stuff Chapter
#  4. Note that print("Hello World!", end="") will print the string Hello
# World! without a newline.
#
# Original Exercise from Automate the Boring Stuff Chapter 4:
# Say you have a list of lists where each value in the inner lists is a
# one-character string, like this:
#
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# You can think of grid[x][y] as being the character at the x- and
# y-coordinates of a “picture” drawn with text characters. The (0, 0) origin
# will be in the upper-left corner, the x-coordinates increase going right,
# and the y-coordinates increase going down.
#
# Copy the previous grid value, and write code that uses it to print the image.
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

if __name__ == '__main__':
    grid = [['.', '.', '.', '.', '.', '.'], ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'], ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'], ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for i in range(len(grid[len(grid) - 1])):
        for j in range(len(grid)):
            print(grid[j][i], end="")
        print("")
