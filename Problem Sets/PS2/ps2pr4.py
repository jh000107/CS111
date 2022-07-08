# 
# ps2pr4.py - Problem Set 2, Problem 4
#
# Fun with recursion, part I
#
#

def mult(n, m):
    """ uses recursion to compute and return the product of intergers, n and m
        inputs: positive integers """
    if n == 0:
        return 0
    else:
        mul_rest = mult(n-1, m)
        return m + mul_rest

def dot(l1, l2):
    """ uses recursion to compute and return the dot product of those lists
        inputs: l1, l2 --> two lists of numbers """
    if len(l1) == len(l2):
        if l1 == '' or l1 == []:
            return 0.0
        else:
            list_rest = dot(l1[1:], l2[1:])
            return l1[0] * l2[0] + list_rest
    else:
        return 0.0

def add_spaces(s):
    """ uses recursion to form and return the string formed by adding a space between each pair of adjacent characters in the string
        input: s --> string """
    if len(s) == 1:
        return s[0]
    else:
        return s[0] + ' ' + add_spaces(s[1:])
        

# test function with a sample test call for functions above
# functions: mult(n, m) ; doc(l1, l2) ; add_spaces(s)
def test():
    """ performs test calls on the functions above """
    print('mult(3, 6) returns', mult(3,6))
    print('mult(4, 5) returns', mult(4,5))
    print('dot([3,4], [2,2]) returns', dot([3,4], [2,2]))
    print('dot([4,5], [2,3]) returns', dot([4,5], [2,3]))
    print('dot([3,4,3], [2,2]) returns', dot([3,4,3], [2,2]))
    print('dot([], []) returns', dot([], []))
    print("add_spaces('hello') returns", add_spaces('hello'))
    print("add_spaces('x') retunrs", add_spaces('x'))

    
    

