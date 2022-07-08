def letter_score(letter):
    """ returns the value of input letter as a scrabble tile
        input: letter --> lower case letter """
    assert(len(letter) == 1)
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    elif letter in ['d', 'g']:
        return 2
    elif letter in ['b', 'm', 'p']:
        return 3
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    elif letter in ['q', 'z']:
        return 10
    else:
        return 0

def scrabble_score(word):
    """ returns the scrabble score of the string, word (sum of the scrabble scor es of its letters)
        input: word --> a string """
    if word == '':
        return 0
    else:
        rest_word = scrabble_score(word[1:])
        return letter_score(word[0]) + rest_word

def num_diff(s1, s2):
    """ returns the number of differences between the two strings
        input: s1, s2 --> strings """
    assert(len(s1) == len(s2))
    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        rest_letters = num_diff(s1[1:], s2[1:])
        if s1[0] == s2[0]:
            return rest_letters
        else:
            return rest_letters + 1

def weave(s1, s2):
    """ returns a new string that is formed by "weaving" together the characters in the strings s1 and s2 to create a single string
        input: s1, s2 --> strings """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    else:
        rest = weave(s1[1:], s2[1:])
        return s1[0] + s2[0] + rest
        

# test function with a sample test call for functions above
def test():
    """ tests for letter_score(letter) """
    print("letter_score('a') returns", letter_score('a'))
    print("letter_score('z') returns", letter_score('z'))
    """ tests for scrabble_score(word) """
    print("scrabble_score('aabq') returns", scrabble_score('aabq'))
    print("scrabble_score('adbfq') returns", scrabble_score('adbfq'))
    """ tests for num_diff(s1, s2) """
    print("num_diff('nice', 'vibe') returns", num_diff('nice', 'vibe'))
    print("num_diff('bad', 'sad') returns", num_diff('bad', 'sad'))
    print("num_diff('same', 'same') returns", num_diff('same', 'same'))
    """ tests for weave(s1, s2) """
    print("weave('aaaa', 'bbbb') returns", weave('aaaa', 'bbbb'))
    print("weave('aaaaaa', 'bbb')  returns", weave('aaaaaa', 'bbb'))
    print("weave('aaa', 'bbbbb') returns", weave('aaa', 'bbbbb'))
    
        
        
