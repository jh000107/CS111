# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# name: 
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def root(x):
    """ returns the square root of its input
        input x: positive number (int or float)
    """
    return x**0.5

# function 2
def gap(num1, num2):
    """ returns the "gap" between the two numbers
        input num1, num2: any number (int or float)
    """
    if num1 > num2:
        return num1 - num2
    elif num1 < num2:
        return num2 - num1
    else:
        return 0

# function 3
def larger_gap(a1, a2, b1, b2):
    """ returns the larger of the two gaps
        input a1, a2, b1, b2: any number (int or float)
    """
    gap1 = gap(a1, a2)
    gap2 = gap(b1, b2)
    if gap1 > gap2:
        return gap1
    elif gap1 < gap2:
        return gap2
    else:
        return gap1

# function 4
def distance(x1, y1, x2, y2):
    """ returns the distance between two points: (x1, y1) and (x2, y2)
        input x1, y1, x2, y2: any number (int or float)
    """
    a = (x1 - x2)**2
    b = (y1 - y2)**2
    c = a + b
    return root(c)


    




# test function with a sample test call for function 0-4
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))
    print('gap(1, 3) returns', gap(1, 3))
    print('larger_gap(1,4,2,6) returns', larger_gap(1,4,2,6))
    print('distance(1,3,1,8) returns', distance(1,3,1,8))

    # optional but encouraged: add test calls for your functions below
