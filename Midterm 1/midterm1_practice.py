def count_ones(s):
    """ returns the number of '1's in the input
        input: s --> string
    """
    if len(s) == 0:
        return 0
    else:
        rest_string = count_ones(s[1:])
        if s[0] == '1':
            return rest_string + 1
        else:
            return rest_string



def swap_bits(s):
    """ swaps each bit in s with the other bit
        input: s --> string containing '0's and '1's
    """
    if s == '':
        return ''
    else:
        rest_bits = swap_bits(s[1:])
        if s[0] == '1':
            return '0' + rest_bits
        else:
            return '1' + rest_bits


        

def num_divisors(n):
    """ returns the number of integers from 1 to n that divide n evenly
        input: n --> integer
    """
    list_divisors = [x for x in range(1, n+1) if n % x == 0]
    return len(list_divisors)



def most_divisors(lst):
    """ returns the integer from that list with the most divisors
        input: list
    """
    y = [[num_divisors(x), x] for x in lst]
    max_pair = max(y)
    return max_pair[1]


def count_transitions(s):
    """ returns the number of times there is a transition
        input: s --> string
    """
    if len(s) <= 1:
        return 0
    else:
        rest_string = count_transitions(s[1:])
        if s[0] == s[1]:
            return rest_string
        else:
            return rest_string + 1



def longest_string(lst):
    """ returns the longest string from lst
        input: lst --> list
    """
    y = [[len(x), x] for x in lst]
    longest_pair = max(y)
    return longest_pair[1]

def longest_string_rec(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        rest_list = longest_string_rec(lst[1:])
        if len(lst[0]) >= len(lst[1]):
            return lst[0]
        else:
            return rest_list


            


