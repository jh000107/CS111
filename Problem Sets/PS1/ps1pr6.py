# 
# ps1pr6.py - Problem Set 1, Problem 6
#
# Functions on strings and lists, part II
#
# name: Junhui Cho
# email: jh00@bu.edu

# function 1
def reverse(s):
    """ returns a string in which the characters of s have been reversed """
    end_character = -1 * len(s) - 1
    answer = s[-1:end_character:-1]
    return answer

# function 2
def begins_with(word, prefix):
    """ returns True if the string word begins with the string prefix, and False otherwise """
    end_character = len(prefix)
    if word[:end_character] == prefix:
        return True
    else:
        return False

# function 3
def flipside(s):
    """ returns a string whose first half is s's second half and whose second half is s's first half """
    standard = len(s) // 2
    if standard % 2 == 1:
        flipped = s[standard:] + s[:standard]
    else:
        flipped = s[standard:] + s[:standard]
    return flipped

# function 4
def adjust(s, length):
    """ returns a string in which the value of s has been adjusted as necessary to produce a string with the specified length """
    s_length = len(s)
    if s_length < length:
        output = ' ' * (length-s_length) + s
        return output
    else:
        output = s[0:length]
        return output

# test function with a sample test call for function 1-4
def test():
    """ performs test calls on the functions above """
    print("reverse('abcdef') returns", reverse('abcdef'))
    print("begins_with('computer', 'comp') returns", begins_with('computer', 'comp'))
    print("begins_with('computer', 'come') returns", begins_with('computer', 'come'))
    print("flipside('homework') returns", flipside('homework'))
    print("flipside('carpets') returns", flipside('carpets'))
    print("adjust('alien', 6) returns", adjust('alien', 6))
    print("adjust('alien', 4) returns", adjust('alien', 4))
    
    
