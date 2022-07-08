#
# Problem Set 8, Problem 3
# jh00@bu.edu
# Markov text generation
#

import random

def create_dictionary(filename):
    """ returns a dictionary of key-value pairs in which:
        each key is a word encountered in the next file
        the corresponding value is a list of words that follow the key word in text file
        input: filename is a string representing the name of a text file
    """
    file = open(filename, 'r')
    text = file.read()
    file.close()
    words = text.split()

    d = {}
    current_word = '$'

    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]   # new key
        else:
            d[current_word] += [next_word]  # adding values to the existing keys 
        
        if next_word[-1] not in '.?!':
            current_word = next_word        # Still same sentence 
        else:
            current_word = '$'              # New sentence
    return d


def generate_text(word_dict, num_words):
    """ generates and prints a string of num_words words
        inputs: word_dict is a dictionary of word transitions
                num_words is a positive integer
    """
    current_word = '$'

    while num_words > 0:
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word, end = ' ')
        if next_word[-1] not in '.?!':
            current_word = next_word
        else:
            current_word = '$'
        num_words -= 1
    print()
        
    
