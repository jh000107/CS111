#
# Name: CS 111 Staff
#
# lab3task2.py
#

def num_consonants(s):
    """ returns the number of consonants in s
        parameter: s is a string of lower-case letters
    """
    print('input is ' + s)
    if s == '':
        return 0
    else:
        num_in_rest = num_consonants(s[1:])
        print('value returned is ' + str(num_in_rest))
        if s[0] not in 'aeiou':
            return num_in_rest + 1
        else:
            return num_in_rest

test_str1 = 'cat'
print(num_consonants(test_str1))

test_str2 = 'hello'
print(num_consonants(test_str2))
