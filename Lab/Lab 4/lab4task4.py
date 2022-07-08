def longest_word(wordlist):
    """ returns the longest word from the wordlist passed in as 
        a parameter
    """
    pairs = [[len(w), w] for w in wordlist]
    bestpair = max(pairs)
    return bestpair[1]


def square(value):
    """ a helper function that takes a value
        and returns its square
    """
    sq = value ** 2
    return sq

def process_squares(values, choice):
    """ use the square helper function above to return one of two possible results
        input: values --> a list of integers ; choice --> a single integer
    """
    pairs = [[square(x), x] for x in values]
    largest_pair = max(pairs)
    return largest_pair[choice-1]
