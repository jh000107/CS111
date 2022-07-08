# 
# ps6pr3.py - Problem Set 6, Problem 3
#
# Processing sequences with loops
#
# This is a pair-optional problem: working alone
#

def add_spaces(s):
    """ uses a loop to return the string formed by adding a space between
        each pair of adjacent characters in the string
        input: s --> an arbitrary string
    """
    result = ''
    for x in range(len(s)):
        if len(s) > 1:
            if x == len(s)-1:
                result += s[x]
            else:
                result += s[x] + ' '
        else:
            result = s
    return result

def num_diff(s1, s2):
    """ uses a loop to return the number of differences between the two strings
        input: s1, s2 --> strings
    """
    count = 0
    len_shorter = min(len(s1), len(s2))
    for i in range(len_shorter):
        if s1[i] != s2[i]:
            count += 1
    count += max(len(s1), len(s2)) - len_shorter
    return count

def negate_odds(values):
    """ modifies the list so that all of its odd_valued elements are replaced
        with their negated values, but even-valued are left unchanged
        input: values --> a list of integers
    """
    for i in range(len(values)):
        if values[i] % 2 == 1:
            values[i] = -1 * values[i]

def find(elem, seq):
    """ uses a loop to return the index of the first occurrence of elem in seq
        input: elem --> element ; seq --> a list or a string
    """
    index = 0
    for x in range(len(seq)):
        if seq[x] == elem:
            index = x
            return index
        else:
            index = -1
    return index


def test1():
    """ tests for the first function
        add_spaces(s)
    """
    print("add_spaces('hello'):", add_spaces('hello'))
    print("add_spaces('hangman'):", add_spaces('hangman'))
    print("add_spaces('x'):", add_spaces('x'))

def test2():
    """ tests for the second function
        num_diff(s1, s2)
    """
    print("num_diff('alien', 'allen'):", num_diff('alien', 'allen'))
    print("num_diff('alien', 'alone'):", num_diff('alien', 'alone'))
    print("num_diff('aliens', 'alone'):", num_diff('aliens', 'alone'))
    print("num_diff('same', 'same'):", num_diff('same', 'same'))
    print("num_diff('same', 'sameness'):", num_diff('same', 'sameness'))

def test3():
    """ tests for the third function
        negate_odds(values)
    """
    vals1 = [1,2,3,4,5,6]
    negate_odds(vals1)
    print('if vals1 = [1, 2, 3, 4, 5, 6]')
    print('negate_odds(vals1) modifies vals1 to ', vals1)

def test4():
    """ tests for the last function
        find(elem, seq)
    """
    print('find(5, [4, 10, 8, 5, 3, 5]):', find(5, [4, 10, 8, 5, 3, 5]))
    print("find('hi', ['well', 'hi', 'there']):", find('hi', ['well', 'hi', 'there']))
    print("find('b', 'banana'):", find('b', 'banana'))
    print("find('i', 'team'):", find('i', 'team'))
    
