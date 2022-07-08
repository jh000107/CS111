#Junhui Cho
#ps3pr4
# More algorithm design!

def find(elem, seq):
    """ uses recursion to find and return the index of the first occurrence of elem in seq
        input: elem --> element ; seq --> a list or a string
    """
    if seq == '':
        return -1
    elif seq == []:
        return -1
    elif seq[0] == elem:
        return 0
    else:
        rest_seq = find(elem, seq[1:])
        if rest_seq >= 0:
            return 1 + rest_seq
        else:
            return -1
                            

def helper(a, b):
    """ helper function for jscore(s1, s2) function
    """
    if a == '' or b == '':
        return ''
    elif b[0] == a:
        return b[1:]
    else:
        rest = helper(a, b[1:])
        return b[0] + rest

def jscore(s1, s2):
    """ returns the Jotto score of s1 compared with s2
        input: s1, s2 --> strings
    """
    if s1 == '' or s2 == '':
        return 0
    elif s1[0] in s2:
        return jscore(s1[1:], helper(s1[0],s2)) + 1
    else:
        return jscore(s1[1:], s2)

def lcs(s1, s2):
    """ returns the longest common subsequence that they share
        input: s1, s2 --> strings
    """
    if s1 == '' or s2 == '':
        return ''
    else:
        if s1[0] == s2[0]:
            return s1[0] + lcs(s1[1:], s2[1:])
        else:
            result1 = lcs(s1[1:], s2)
            result2 = lcs(s1, s2[1:])
            if len(result1) <= len(result2):
                return result2
            elif len(result1) >= len(result1):
                return result1

print(find(5, [4, 10, 5, 3, 7, 5]))
print(find('hi', ['well', 'hi', 'there']))
print(find('b', 'banana'))
print(find('a', ''))

print(jscore('diner', 'syrup'))
print(jscore('always', 'walking'))

print(lcs('human', 'chimp'))
print(lcs('gattaca', 'tacgaacta'))
    
