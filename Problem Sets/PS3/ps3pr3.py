# Junhui Cho
# ps3pr3.py (Problem Set 3, Problem 3)        
#
# Caesar cipher / decipher
#

# A template for a helper function called rot that we recommend you write
# as part of your work on the encipher function.
def rot(c, n):
    """ rotates a single character c forward by n spots in the alphabet
        inputs: c --> string ; n --> positive integer
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.
    if 'a' <= c <= 'z':
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
    elif 'A' <= c <= 'Z':
        new_ord = ord(c) + n
        if new_ord > ord('Z'):
            new_ord = ord(c) + n
            if new_ord > ord('Z'):
                new_ord = new_ord - 26
    else:
        new_ord = ord(c)

    return chr(new_ord)
            
            


### Put your code for the encipher function below. ###
def encipher(s, n):
    """ retunrs a new string in which the letters in s have been "rotated" by n characters forward in the alphabet, wrapping around as needed
        inputs: s --> string ;  n --> non-negative integer
    """
    assert(0 <= n <= 25)
    if len(s) == 0:
        return ''
    else:
        return rot(s[0], n) + encipher(s[1:],n)
    
    

        

# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_prob(c):
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

### letter_prob for not just a single character, but for sum of all probabilities of characters in a sentece ###
def letter_prob_mod(string):
    if len(string) == 0:
        return 0
    else:
        rest_string = letter_prob_mod(string[1:])
        return letter_prob(string[0]) + letter_prob_mod(string[1:])

#### Put your code for the decipher function below. ####    

def decipher(s):
    # I could not figure out the list of list part where I think we were supposed to make a list contatining the probablity and the index of it.
    """ returns the original English string, which will be some rotation of the s
        input: s --> string
    """
    possible_deci = [encipher(s,n) for n in range(26)]
    assign_score = [[letter_prob_mod(x),x] for x in possible_deci]
    max_score = max(assign_score)
    likely = max_score[1]
    output = encipher(s, likely)
    return output

print(rot('a',1))
print(rot('y',2))

print(encipher('xyza', 1))
print(encipher('Caesar cipher? I prefer Caesar salad.', 25))

print(decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.'))
