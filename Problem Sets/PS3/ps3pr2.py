def cube_all_lc(values):
    """ uses a list comprehension to create and return a list containing the cubes of the numbers in values
        input: values --> a list of numbers """
    [x**3 for x in values]
    return x

def cube_all_rec(values):
    """ uses recursion to create and return a list containing the cubes of the numbers in values
        input: values --> a list of numbers """
    rest_cube = cube_all_rect(values[1:])
    return [values[0] ** 3]

def num_larger(threshold, values):
    """ returns the number of elememnts of values that are larger than threshold
        inputs: threshold --> a number ; values --> list of numbers """
    return sum([1 for x in values if x > threshold])

def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_consonants(words):
    """ returns the string in the list with most consonants
        input: a list of strings """
    num_conso_word_list = [[len(x) - num_vowels(x), x] for x in words]
    max_consonants = max(num_conso_word_list)
    return max_consonants[1]

def price_string(cents):
    """ returns a string in which the price is expressed as a combination of dollars and cents
        input: cents --> positive integer """
    d = cents // 100   # compute whole number of dollars
    c = cents % 100    # compute remaining cents

    price = ''            # initial value of the price string
    if d == 0:
        if c == 1:
            price = price + str(c) + ' cent'
        else:
            price = price + str(c) + ' cents'
    elif c == 0:
        if d == 1:
            price = price + str(d) + ' dollar'
        else:
            price = price + str(d) + ' dollars'
    elif d == 1:
        if c == 1:
            price = price + str(d) + ' dollar, ' + str(c) + ' cent'
        else:
            price = price + str(d) + ' dollar, ' + str(c) + ' cents'
    elif c == 1:
        if d > 1:
            price = price + str(d) + ' dollars, ' + str(c) + ' cent'
    else:
        price = price + str(d) + ' dollars, ' + str(c) + ' cents'
    return price
