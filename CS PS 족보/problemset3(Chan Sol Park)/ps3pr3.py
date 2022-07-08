#Chan Sol Park
#chansol@bu.edu
#CS111

#function 0
def cube_vals_lc(values):
            """using list comprehension, it gets a list of values and
               cubes each value
            """
            x = [x**3 for x in values]
            return x

#function 1
def cube_vals_rec(values):
            """using recursion, it gets a list of values and
               cubes each value
            """
            if values == []:
                        return []
            else:
                        x = [values[0]**3] + cube_vals_rec(values[1:])
                        return x

#function 2
def num_greater(threshold, values):
            """it gets a threshold value and list of values then outputs
               how many numbers in the list are larger than the threshold
               value
            """
            x = [y for y in values if y > threshold]
            return len(x)

#function 3
def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
        This is a helper function for most_vowels
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_vowels(wordlist):
            """gets a list of words and outputs the word that has
               most vowels in it
            """
            if wordlist == []:
                        return []
            else:
                        x = [num_vowels(n) for n in wordlist]
                        y = max(x)
                        m = wordlist[y]
                        return m

print("function 0 outputs", cube_vals_lc([1,-2,3,-4,5]))
print("function 1 outputs", cube_vals_rec([1,-2,3,-4,5]))
print("function 2 outputs", num_greater(2, [3, 5, 2, 10]))
print("function 3 outputs", most_vowels(['hello', 'there', 'computer', 'science']))
