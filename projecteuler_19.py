"""
projecteuler_19.py

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

- Calculate 100!
- Convert integer to string
- Separate string into array (1 char per field)
- Sum array
- Return result

This is very similar to problem 16, so I'll be reusing plenty of code from that.
Never reinvent the wheel.

Here's the code written in long form with some printed sanity checks: below is the one-line condensed version.

integer = math.factorial(100)   #   calculate 100!, assign that value to integer

print(integer)  

string = str(integer)   # convert the integer into a string, stored in string

array = [int(x) for x in str(string)]   # convert the string into an array of integers

print(array)

result = sum(array)

print(result)


"""

import math

print(sum([int(x) for x in (str(math.factorial(100)))]))
