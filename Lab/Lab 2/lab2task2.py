def mysum(x, y):
    """ takes two numbers and returns their sum """
    total = x + y
    return total
mysum(44, 67)
print(mysum(10,7))

def sum_double(x, y):
    """ takes two numbers and returns their sum if they are same but if they are not, returns double the sum"""
    if x == y:
        output = (x+y) * 2
    else:
        output = x + y
    return output

def test():
    """ function for testing """
    test1 = sum_double(1, 2)
    print('first test returns', test1)

    # Add more tests below
    
    test2 = sum_double(2, 2)
    print('second test sum_double(2, 2) returns', test2)
