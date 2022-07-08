#
# ps6pr4.py - Problem Set 6, Problem 4
# 
# Definite vs. indefinite loops
#
# individual
#

def log(b, n):
    """ uses a loop to return the logarithm to the base b of a number n
        inputs: b,n --> positive integers
    """
    count = 0
    div = n
    while div > 1:
        print('dividing', div, 'by', b, 'gives', div//b)
        div = div // b
        count += 1
    return count
        
        
def add_powers(m, n):
    """ uses a loop to add together the first m powers of n and returns the resulting sum
        input: m --> a positive integer ; n --> an arbitrary integer
    """
    count = 0
    sum_powers = 0
    while m > 0:
        powers = n**count
        print(n, '**', count, '=', powers)
        sum_powers += powers
        count +=1
        m -= 1
    return sum_powers

def test1():
    """ tests for the first function
        log(b, n)
    """
    print('log(5, 125) =', log(5, 125))
    print()
    print('log(5, 1) =', log(5, 1))
    print()
    print('log(2, 20) =', log(2, 20))

def test2():
    """ tests for the second function
        add_powers(m, n)
    """
    print('add_powers(4, 2) =', add_powers(4, 2))
    print()
    print('add_powers(6, 3) =', add_powers(6, 3))
