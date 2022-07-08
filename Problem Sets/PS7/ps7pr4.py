#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Matrix Operations  
#
# Computer Science 111   
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###

def mult_row(matrix, r, m):
    """ multiplies row r of the specified matrix by the specified multiplier m
        inputs: maxtrix --> a rectangular 2-D list of numbers
                r --> a number that represents the row number
                m --> a number thhat represents a multiplier
    """
    for c in range(len(matrix[r])):
        matrix[r][c] *= m

def add_row_into(matrix, source, dest):
    """ adds each element of the row with index source to the corresponding
        element of the row with index dest
        inputs: matrix--> a 2-D list of numbers
                source--> index number
                dest--> index number
    """
    for c in range(len(matrix[dest])):
        matrix[dest][c] += matrix[source][c]

def add_mult_row_into(matrix, m, source, dest):
    """ takes the specified 2-D list matrix and adds each element of row source
        , multiplied by m, to the corresponding element of row dest
        inputs: matrix is a 2-D list
                m is a multiplier
                source is an index number
                dest is an index number
    """
    for c in range(len(matrix[source])):
        matrix[dest][c] += matrix[source][c] * m

def transpose(matrix):
    """ takes the specified 2-D list matrix and creates and returns
        a new 2-D list that is the ranspose of matrix
        input: matrix is a 2-D list of numbers
    """
    new_matrix = []
    for r in range(len(matrix[0])):
        row = [0] * len(matrix)
        new_matrix += [row]

    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            new_matrix[r][c] = matrix[c][r]
    return new_matrix

    

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)

        ## add code to handle the other options here
        elif choice == 2:
            r = int(input('Index of row:'))
            m = float(input('Multiplier:'))
            mult_row(matrix, r, m)
        elif choice == 3:
            source = int(input('Index of source row:'))
            dest = int(input('Index of destination row'))
            add_row_into(matrix, source, dest)
        elif choice == 4:
            source = int(input('Index of source row:'))
            dest = int(input('Index of destination row:'))
            m = float(input('Multiplier:'))
            add_mult_row_into(matrix, m, source, dest)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
