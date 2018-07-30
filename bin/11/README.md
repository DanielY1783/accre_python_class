## Exercises

1. Write a generator function that returns the next X Tuesdays as datetime.datetime objects for midnight on that Tuesday.
	* Use this to find out how many Tuesdays there are in 2025.
2. Make a similar “infinite generator” that endlessly returns Tuesdays.
	* Use this infinite generator to determine the date of the last Tuesday in 2056
3. Write a generator expression that returns the square root of the first 10M even integers.
	* Use this in a for loop with enumerate to find the integer for which the sum of all previous square roots is at least 10000
	* Try this again using a list comprehension rather than a generator expression and note the difference in performance. Explain why the generator expression version is so much faster.