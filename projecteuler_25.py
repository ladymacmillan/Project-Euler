"""
projecteuler_25.py

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

I'm sure there's a more computationally elegant way to solve this problem, but at first
blush, it seems like the easiest (cognitively) way to approach it is as follows:

Calculate fibonacci terms
Test len(term)
If len(term) >= 1000, stop and return the answer
Otherwise, keep going

"""

x = 0

fibonacci_last = 1                                  # initialize fibonacci_last as the first fibonacci number           

count = 2                                           # initialize count to 2: we're starting with the second term

fibonacci_new = 1                                   # initialize fibonacci_new to the second fibonacci number

fibonacci_placeholder = 1                           # we need one more term to act as a placeholder

while len(str(fibonacci_new)) < 1000:
    fibonacci_placeholder = fibonacci_new
    fibonacci_new += fibonacci_last
    fibonacci_last = fibonacci_placeholder
    count += 1

print("The index of the answer term is: ", count)
print("The term itself is: ", fibonacci_new)
print("The term length is: ", len(str(fibonacci_new)))
