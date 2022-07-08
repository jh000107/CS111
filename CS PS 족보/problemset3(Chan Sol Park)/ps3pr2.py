#
# ps3pr2.py (Problem Set 3, Problem 2)
#
# Caesar cipher / decipher
#

# A template for a helper function called rot that we recommend writing
# as part of your work on the encipher function.
def rot(c, n):
    """ your docstring goes here """
    assert(type(c) == str and len(c) == 1)


#### Put your code for the encipher function below. ####
def encipher(s, n):
    """gets a word s and moves/rotates each letter position by adding n to its
       position"""
    if s == '':
        return ''
    else:
        if ('a' <= s[0] <= 'z'):
            x = ord(s[0]) + n
            if x > 122:
               x = x - 26
            y = chr(x) + encipher(s[1:],n)
            return y
        elif ('A' <= s[0] <= 'Z'):
           x = ord(s[0]) + n
           if x > 90:
              x = x - 26
           y = chr(x) + encipher(s[1:],n)
           return y
        else:
           y = s[0] + encipher(s[1:],n)
           return y
        
print(encipher('hello', 2))

# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_probability(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####
def helper(s):
    if s == '':
        return 0
    else:
        y = letter_probability(s[0]) + helper(s[1:])
        return y
    #gets the string and gives the letter probability value to each letter

def decipher(s):
    """gets a string and decipher that string so it makes sense in English
    """
    if s == '':
        return ''
    else: 
        options = [encipher(s, n) for n in range(26)]  
        scored_options = [helper(x) for x in options]
        bestscore = max(scored_options)
        index = scored_options.index(bestscore)
        y = encipher(s, index) 
        return y
    #gets the possible outputs for the string within rotating each letter by 1-26
    #convert each string's letters into letter probability values and combine the values.
    #find out the highest value in the list
    #find the position of that number in the list
    #output the string that is located at that position

print(decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj'))
