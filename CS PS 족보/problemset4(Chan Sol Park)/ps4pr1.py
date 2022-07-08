# ps4pr1.py - Problem Set 4, Problem 1
#
# From binary to decimal and back!
#
# name: Chan Sol Park
# email: chansol@bu.edu

#function 0
def dec_to_bin(n):
            """gets an integer value and returns its binary value"""
            result = ''
            if n == 1:
                        return result + '1'
            elif n == 0:
                        return result + '0'
            else:
                        if n%2 == 1:
                                    return dec_to_bin(n//2) + result + '1'
                        elif n%2 == 0:
                                    return dec_to_bin(n//2)+ result + '0'
                        
                        
#function 1
def bin_to_dec(b):
            """gets a string of a binary value and return its decimal
               value
            """
            if b == '1':
                        return 1
            elif b == '0':
                        return 0
            else:
                        if b[-1] == '0':
                                    return 2*bin_to_dec(b[:-1])
                        else:
                                    return 2*bin_to_dec(b[:-1])+1

#sample test call for function 0
print('test function#0 def_to_bin(1011) returns', dec_to_bin(11))
                                    
#sample test call for function 1
print('test function#1 bin_to_def(1111111) returns', bin_to_dec('1011'))
