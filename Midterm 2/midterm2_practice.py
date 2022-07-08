def years_needed(principal, rate, target):
    """ determines the number of years compounded annual interest that are
        needed for the investment to reach or exceed the specified target
    """
    num_years = 0
    while principal <= target:
        principal *= (1 + rate)
        num_years += 1
    return num_years

def count_vowels(s):
    """ returns the number of vowels in a string
        input: s is a string
    """
    count = 0
    for x in s:
        if x in 'aeiou':
            count += 1
    return count

def stars(n):
    """ prints n lines of stars with 1 star on first line, 2 starts on
        secoond line, and so forth
        input: n is a positive integer
    """
    for x in range(n):
        output = '*' * (x+1)
        print(output)

def all_perfect(lst):
    """ returns True if all of the numbers are 100
        input: lst is a list of numbers
    """
    count = 0
    for x in lst:
        if x != 100:
            count += 1
    if count == 0:
        return True
    else:
        return False

def index_nearest(n, lst):
    """ returns the index of the element in lst whose value is closest to n
        inputs: n is a number
                lst is a list of numbers
    """
    a = abs(lst[0] - n)
    nearest = 0
    for x in range(len(lst)):
        diff = abs(lst[x] - n)
        if diff <= a:
            nearest = x
    return nearest

def num_appearances(substring, s):
    """ returns the number of appearances of the specified substring
        inputs: substring is a string of length 2
                s is a string
    """
    count = 0
    for x in range(len(s)-1):
        if s[x:x+2] == substring:
            count += 1
    return count

def most_common_pair(s):
    most = num_appearances(s[:2], s)
    substring = ''
    for x in range(len(s)-1):
        if num_appearances(s[x:x+2], s) >= most:
            most = num_appearances(s[x:x+2], s)
            substring = s[x:x+2]
    return substring

            
            

