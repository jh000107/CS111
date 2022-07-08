def min_val(values):
    """ Takes a non-empty list of values and uses recursion to find and return the smallest value in the list"""
    if len(values) == 1:
        return values[0]
    else:
        remain_vals = min_val(values[1:])
        if values[0] < remain_vals:
            return values[0]
        else:
            return remain_vals

def test():
    """ test function for min_val() """
    test1 = min_val(['b', 'a', 'c'])
    print('test call 1 returns', test1)
    test2 = min_val([15, 6, 8, 19, 20])
    print('test call 2 returns', test2)
    test3 = min_val([5, 6, 9])
    print('test call 3 returns', test3)

