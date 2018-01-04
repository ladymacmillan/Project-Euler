"""
projecteuler_16.py

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

- Calculate 2^1000
- Convert integer to string
- Separate string into array (1 char per field)
- Sum array
- Return result

The integer has to be converted to a string because int objects are not iterable. Then the elements of the array
generated from the string have to be converted back into integers, because sum can't take string values.
If this seems silly, it's OK, there are good reasons why we can't just do anything we want with any variable
we want whenever we want. That would be madness and anarchy.

Here's the code written in long form with some printed sanity checks: below is the one-line condensed version.

integer = 2**1000   #   calculate 2^1000, assign that value to integer

print(integer)  

string = str(integer)   # convert the integer into a string, stored in string

array = [int(x) for x in str(string)]   # convert the string into an array of integers

print(array)

result = sum(array)

print(result)


"""

print(sum([int(x) for x in (str(2**1000))]))
