# PS4PR2
# Junhui Cho
# CS111

from ps4pr1 import *

def mul_bin(b1, b2):
    """ multiplies the numbers and returns the result in the form of a string that represents a binary number
        inputs: b1, b2 --> strings
    """
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    b = dec_to_bin(n1*n2)
    return b

def add_bytes(b1, b2):
    """ compute the sum of the two bytes and return that sum in the form of a string that represents an 8-bit binary number
        input: b1, b2 --> two strings that represent bytes (8-bit)
    """
    sum_n1_n2 = bin_to_dec(b1) + bin_to_dec(b2)
    b = dec_to_bin(sum_n1_n2)
    len_b = len(b)
    if len_b > 8:
        return b[1:]
    elif len_b < 8:
        return '0' * (8-len_b) + b

# tests for functions above
def test():
    """ tests for functions mul_bin(b1, b2) and add_bytes(b1, b2)
    """
    print("mul_bin('11', '10') returns ", mul_bin('11', '10'))
    print("add_bytes('00000011', '00000001') returns", add_bytes('00000011', '00000001'))


