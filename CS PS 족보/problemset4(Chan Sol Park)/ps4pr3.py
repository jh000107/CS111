# ps4pr3.py - Problem Set 4, Problem 3
#
# Recursive operations on binary numbers
#
# name: Chan Sol Park
# email: chansol@bu.edu

#function 0
def bitwise_and(b1, b2):
            """gets 2 strings that are binary values and using recursion, it returns
               the computed bitwise AND of the 2 strings
            """
            result = ''
            if (b1 == '') and (b2 == ''):
                        return ''
            elif b1 == '':
                        return bitwise_and('0',b2)
            elif b2 == '':
                        return bitwise_and(b1,'0')
            else:
                        if b1[-1] == '1':
                                    if b2[-1] == '1':
                                                return result + bitwise_and(b1[:-1], b2[:-1])+'1'
                                    elif b2[-1] == '0':
                                                return result + bitwise_and(b1[:-1], b2[:-1])+'0'
                             
                        if b1[-1] == '0':
                                    if b2[-1] == '1':
                                                return result + bitwise_and(b1[:-1], b2[:-1])+'0'
                                    elif b2[-1] == '0':
                                                return result + bitwise_and(b1[:-1], b2[:-1])+'0'
                                    

#function 1
def add_bitwise(b1, b2):
            """gets 2 strings of binary values and add them using recursion, returning result
               as also a binary value
            """
            if b1 == '':
                        return b2
            elif b2 == '':
                        return b1
            else:
                        rest = add_bitwise(b1[:-1], b2[:-1])
                        if b1[-1] == '1':
                                    if b2[-1] == '1':
                                                return add_bitwise(rest, '1')  + '0' 
                                    elif b2[-1] == '0':
                                                return rest + '1'
                        elif b1[-1] == '0':
                                    if b2[-1] == '1':
                                                return rest + '1' 
                                    elif b2[-1] == '0':
                                                return rest + '0'

#sample test call for function 0
print('ps4pr3 test function#0 bitwise_and("1001111","11011") returns', bitwise_and('1001111','11011'))
#sample test call for function 1
print('ps4pr3 test function#1 add_bitwise("11","100") returns', add_bitwise('11','100'))

