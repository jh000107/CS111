#
# Lab 4, Task 2 - debugging a recursive function
#

def count(val, values):
    """ returns the number of times that val is found in the list values
        parameters:
            val -- an arbitrary value
            values -- a list of 0 or more arbitrary values
    """
    if len(values) == 0:
        return 0
    else:
        count_in_rest = count(val, values[1:])
        if values[0] == val:
            return count_in_rest + 1
        else:
            return count_in_rest
