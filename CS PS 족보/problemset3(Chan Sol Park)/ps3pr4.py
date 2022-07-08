#Chan Sol Park
#chansol@bu.edu
#CS111

#function 0
def index_last(c, s):
            """gets a string s and a single letter c. Then outputs the position
               value where c lastly occurs in string s.
            """
            if c == '':
                        return -1
            if s == '':
                        return -1
            else:
                        if c == s[-1]:
                                    x = s[:-1]
                                    return len(x)
                        else:
                                    return index_last(c, s[:-1])       

#function 1
def helper(x1, x2):
            """helper function for jscore function"""
            if (x1 == '') or (x2 == ''):
                        return ''
            elif x2[0] == x1:
                        return x2[1:]
            else:
                        rest = helper(x1, x2[1:])
                        return x2[0] + rest
            
def jscore(s1, s2):
            """gets 2 strings and returns the jotto score by comparing
               the given strings.
            """
            if (s1 == '') or (s2 == ''):
                        return 0
            elif s1[0] in s2:
                        return jscore(s1[1:], helper(s1[0],s2)) + 1
            else:
                        return jscore(s1[1:], s2) 

#function 2
def lcs(s1, s2):
            """gets two strings and returns the lcs string of those two
               strings.
            """
            if (s1 == '') or (s2 == ''):
                        return ''
            else:
                        if s1[0] == s2[0]:
                                    return s1[0] + lcs(s1[1:], s2[1:])
                        else:
                                  result1 = lcs(s1[1:], s2)
                                  result2 = lcs(s1, s2[1:])
                                  if len(result1) >= len(result2):
                                              x = result1
                                              return x
                                  elif len(result2) >= len(result1):
                                              x = result2
                                              return x
print('function 0 outputs', index_last('r', 'terriers'))
print('function 1 outputs', jscore('recursion','excursion'))
print('function 2 outputs', lcs('abcdefgh','efghabcd'))
