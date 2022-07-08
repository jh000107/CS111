# 
# ps2pr2.py - Problem Set 2, Problem 2
#
# More practice writing non-recursive functions
#
# This is an individual-only problem that you must complete on your own.
#

def move_to_end(s, n):
    """ returns a new string in which the first n characters of s have been moved to the end of the string
        inputs: s = string; n = non-negative integers """
    if n >= len(s):
        return s
    else:
        s_rest = s[n:]
        return s_rest + s[:n]


def repeat_elem(values, index, num_times):
    """ returns a new list in which the element of values at position index has been repeated num_times tims
        inputs: values = list; index = integer; num_times = positive integer """
    if index >= 0:
        return values[:index] + [values[index]] * num_times + values[index+1:]
    else:
        return values[:index] + [values[index]] * num_times + values[len(values)+index+1:]


# test function with a sample test call for functions above
def test():
    """ performs test calls on the function move_to_end(n, s) """
    print("move_to_end('computer', 3) returns", move_to_end('computer', 3))
    print("move_to_end('computer', 0) returns", move_to_end('computer', 0))
    print("move_to_end('computer', 10) returns", move_to_end('computer', 10))
    """ performs test calls on the function repeat_elem(values, index, num_times """
    print('repeat_elem([10,11,12,13], 2, 4) returns', repeat_elem([10,11,12,13], 2, 4))
    print('repeat_elem([10,11,12,13], -3, 4) returns', repeat_elem([10,11,12,13], -3, 4))
    print('repeat_elem([10,11,12,13,14,15], -2, 5) returns', repeat_elem([10,11,12,13,14,15], -2, 5))
    print('repeat_elem([10,11,12], -3, 8) returns', repeat_elem([10,11,12], -3, 8))

