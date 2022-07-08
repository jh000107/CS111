# Junhui Cho
# ps4pr3
# CS111

def bitwise_and(b1, b2):
    """ use recursion to compute the bitwise AND of the two numbers and return the result in the form of a stirng
        input: b1, b2 --> strings
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return len(b2) * '0'
    elif b2 == '':
        return len(b1) * '0'
    else:
        rest_bitwise_and = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return rest_bitwise_and + '1'
        else:
            return rest_bitwise_and + '0'


def add_bitwise(b1, b2):
    """ use recursion to perform the bitwise addition algorithm
        inputs: b1, b2 --> strings (binary numbers)
    """
    if b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        rest_sum = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == b2[-1]:
            if b1[-1] == '0':
                return rest_sum + '0'
            elif b1[-1] == '1':
                return add_bitwise(rest_sum, '1') + '0'
        else:
            return rest_sum + '1'

# Test function for functions above
# bitwise_and(b1,b2) and add_bitwise(b1,b2)
def test():
    print("bitwise_and('11010', '10011') returns", bitwise_and('11010', '10011'))
    print("bitwise_and('1001111', '11011') returns", bitwise_and('1001111', '11011'))

    print("add_bitwise('11100', '11110') returns", add_bitwise('11100', '11110'))
    print("add_bitwise('10101', '10101') returns", add_bitwise('10101', '10101'))
