#
# ps2pr6.py - Problem Set 2, Problem 6
#
# list comprehensions
#

# Problem 6-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [ x+7 for x in range(5)]
print(lc1)

# part b
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [ w[-1] for w in words]
print(lc2)

# part c
lc3 = [ word[::2] for word in ['hello', 'bye', 'no']]
print(lc3)

# part d
lc4 = [ x for x in range(1, 20) if x % 6 == 0]
print(lc4)

# part e
lc5 = [ c == 'a' for c in 'aardvark']
print(lc5)


# Problem 5-2: Put your definition of the powers_of() function below.
def powers_of(base, count):
    """ returns a list containing the first count powers of base, beginning with the 0th power.
        input: base --> number; count --> positive integer"""
    return [base ** x for x in range(count)]


# Problem 5-3: Put your definition of the starts_with() function below.
def starts_with(prefix, wordlist):
    """ returns a list consisting of all words from wordlist that begin with prefix
        inputs: prefix --> string; wordlist --> list of strings """
    return [x for x in wordlist if x[:len(prefix)] == prefix]


# test function with a sample test call for functions 5-2, 5-3
def test():
    """ performs test calls on the function powers_of(base, count) """
    print('powers_of(3, 4) returns', powers_of(3,4))
    """ performs test calls on the function starts_with(prefix, wordlist) """
    print("starts_with('fun', ['functions', 'are', 'really', 'fun!'] returns", starts_with('fun', ['functions', 'are', 'really', 'fun!']))


