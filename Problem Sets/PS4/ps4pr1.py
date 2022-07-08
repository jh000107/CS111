# Problem Set 4, Problem 1
# Junhui Cho
# CS 111
# From binary to decimal and back

def dec_to_bin(n):
    """ uses recursion to convert it from decimal to binary
        input: n --> non-negative integer
    """
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        rest_n = n >> 1
        if n % 2 == 1:
            return dec_to_bin(rest_n) + '1'
        else:
            return dec_to_bin(rest_n) + '0'


def bin_to_dec(b):
    """ uses recursion to convert the number from binary to decimal
        input: b --> string
    """
    if b == '0':
        return 0
    elif b == '1':
        return 1
    else:
        rest_b = bin_to_dec(b[:-1])
        if b[-1] == '0':
            return 2 * rest_b
        else:
            return 2 * rest_b + 1

# tests for functions above
# dec_to_bin(n) and bin_to_dec(b)
def test():
    """ tests for functions above
    """
    print("dec_to_bin(7) returns", dec_to_bin(7))
    print("bin_to_dec('00011010') returns", bin_to_dec('00011010'))
