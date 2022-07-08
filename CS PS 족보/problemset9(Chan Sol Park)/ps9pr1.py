# 
# ps9pr1.py - Problem Set 9, Problem 1
#
# Using String Methods
#
# name: Chan Sol Park
# email: chansol@bu.edu
#

def count_ignore_case(s, sub):
            """takes a string s and a substring sub, and uses string methods
               to compute and return the number of occurences of sub in s,
               but in a way that ignores the cases of the letters involved/
            """
            s = s.upper()
            sub = sub.upper()
            return s.count(sub)

def middle_name(fullname):
            """takes a string fullname that represents a person’s full name,
               and that uses one or more string methods to extract and return
               a string representing the person’s middle name.
            """
            if fullname.count(' ') <= 1:
                        return ''
            else:
                        string = fullname.split()
                        return string[1]
