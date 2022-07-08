# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part I
#
# name: Junhui Cho
# email: jh00@bu.edu

# function 1
def outer_vals(values):
    """ put your docstring here """
    first = values[0]
    last = values[-1]
    return [first, last]

# function 2
def ends_match(s):
    """ checks if first and last character matches """
    if s[0] == s[-1]:
        return True
    else:
        return False

# function 3
def every_other(values):
    """ returns a list containing every other value from the original list """
    a = values[::2]
    return a

# test function with a sample test call for function 1-3
def test():
    """ performs test calls on the functions above """
    print('outer_vals([1, 2, 3, 4, 5, 1]) returns', outer_vals([1, 2, 3, 4, 5, 1]))
    print("ends_match('satisfies') returns", ends_match('satisfies'))
    print('every_other([1, 2, 3, 4, 5]) returns', every_other([1, 2, 3, 4, 5]))

    
 

        
