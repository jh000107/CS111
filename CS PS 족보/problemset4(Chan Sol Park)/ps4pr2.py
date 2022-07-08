# ps4pr2.py - Problem Set 4, Problem 2
#
# Using your conversion functions
#
# name: Chan Sol Park
# email: chansol@bu.edu

from ps4pr1 import*
                        
#function 0
def add(b1, b2):
            """gets two stings of binary values. Add their values and
               return their result in binary
            """
            n1 = bin_to_dec(b1)
            n2 = bin_to_dec(b2)
            b_sum = dec_to_bin(n1+n2)
            return b_sum

#function 1
def add_bytes(b1, b2):
            bintodec1 = bin_to_dec(b1)
            bintodec2 = bin_to_dec(b2)
            addition = dec_to_bin(bintodec1 + bintodec2)
            addlen = len(addition)
            if addlen > 8:
                        return addition[addlen - 8:]
            elif addlen < 8:
                        return (8 - addlen)*'0'+addition
            else:
                        addition
#sample test call for function 0
print('ps4pr2 test function#0 add("11100", "1110") returns', add('11100','11110'))
#sample test call for function 1
print('ps4pr2 test function#1 add("00000111") returns', increment('00000111'))
