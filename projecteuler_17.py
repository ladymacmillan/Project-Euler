"""
projecteuler_17.py

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage.

This is basically an exercise in formulating rules and detecting edge cases.
Highly recommend outputting all numbers to print in order to more easily review these.

I'm going to focus on function over form here. I'll make it work first, and look at cute little
code optimizations later. Don't get off into the weeds. Comprehensibility over calculation time,
especially when I have to remember what I was doing later.

The integers of 1-9 have their own names, and we'll define them as such:
num_name = "one, two, three, four, five, six, seven, eight, nine"

Ten is a special case. It doesn't have anything added to it, but it gets added to other things.

To make the numbers 13-19, you take a prefix (we'll call it teen_prefix) and append "teen".
teen_prefix = "thir, four, fif, six, seven, eigh, nine" and output to (teens)

11, and 12 are unique words.
uniques = "eleven, twelve"

To make the divisible-by-ten numbers 20 through 90, you take a prefix (tens_prefix) and append "ty".
tens_prefix = "twen, thir, for, fif, six, seven, eigh, nine"
To make further counting easier, output the results of this to an array (ten_name).

To make the whole numbers between each divisible-by-ten number, take the ten_name
and iterate over the num_names, output results to an array (names_under_hundred)

To make the numbers 100, 200, etc., concatenate num_name + "hundred" and output into (hundred_name).

To make the numbers between each hundred, concatenate hundred_name + "and" + [num_name, teens, uniques, ten_name,
names_under_hundred] and output into (numbers_between_hundreds)

One thousand is its own word, but it shouldn't be concatenated with anything else, so we'll just add it at the end.

"""

num_name = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]     # defines the single numbers

teen_prefix = ["thir", "four", "fif", "six", "seven", "eigh", "nine"]                   # defines prefixes for 'teens'

uniques = ["eleven", "twelve"]                                                          # defines unique numbers

thousand = "onethousand"

tens_prefix = ["twen", "thir", "for", "fif", "six", "seven", "eigh", "nine"]            # defines prefixes for 'tens'

teens = [x + "teen" for x in teen_prefix]                                               # concatenates teens

ten_name = [x + "ty" for x in tens_prefix]                                              # concatenates tens

names_under_hundred = []

for x in ten_name:                                                                      # concatenates numbers between
    for y in num_name:                                                                  # the tens that are under 100
        result = x + y
        names_under_hundred.append(result)


hundred_name = [x + "hundred" for x in num_name]                                        # concatenates the hundreds

ten_name.append("ten")                                                                  # add in the number 10 itself
                                                                                        # AFTER other things are calculated
numbers_between_hundreds = []

for x in hundred_name:
    for y in num_name:
        result = x + "and" + y
        numbers_between_hundreds.append(result)                                         # concatenates 101, 102, etc.
    for y in teens:
        result = x + "and" + y
        numbers_between_hundreds.append(result)                                         # concatenates 113, 114, etc.
    for y in uniques:
        result = x + "and" + y
        numbers_between_hundreds.append(result)                                         # concatenates 111, 112, etc.
    for y in ten_name:
        result = x + "and" + y
        numbers_between_hundreds.append(result)                                         # concatenates 110, 120, etc.
    for y in names_under_hundred:
        result = x + "and" + y
        numbers_between_hundreds.append(result)                                         # concatenates 121, 122, etc.

all_numbers = []                                                                        # puts all numbers into one array
for x in num_name:
    all_numbers.append(x)

for x in uniques:
    all_numbers.append(x)

for x in teens:
    all_numbers.append(x)

for x in ten_name:
    all_numbers.append(x)

for x in names_under_hundred:
    all_numbers.append(x)

for x in hundred_name:
    all_numbers.append(x)

for x in numbers_between_hundreds:
    all_numbers.append(x)

all_numbers.append(thousand)

all_numbers_len = len(''.join(str(x) for x in all_numbers))                     # length of all numbers in characters

print ("The total is:")
print (all_numbers_len)
