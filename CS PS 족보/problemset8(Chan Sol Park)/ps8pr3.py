#
# ps8pr3.py (Problem Set 8, Problem 3)
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
        input: matrix is a 2-D list numbers
    """
    ## You will revise this function.
    height = len(matrix)
    width = len(matrix[0])
    for r in range(height):
        for c in range(width):
            print('%7.2f' % matrix[r][c], end=' ')
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
    """gets a matrix and multiple every value in the row r by the value m."""
    height = len(matrix)
    width = len(matrix[0])
    for x in range(height):
        for y in range(width):
            if x == r:
                matrix[x][y] = matrix[x][y]*m
    
def add_row_into(matrix, rs, rd):
    """gets a matrix and add values from rs to values into rd values
       individually."""
    height = len(matrix)
    width = len(matrix[0])
    for x in range(height):
        for y in range(width):
            if x == rd:
                matrix[x][y] = matrix[x][y] + matrix[rs][y]
    
def add_mult_row_into(matrix, m, rs, rd):
    """gets a matrix and add each element of row rs, multiplied by m,
       to the corresponding element or row rd.
    """
    height = len(matrix)
    width = len(matrix[0])
    for x in range(height):
        for y in range(width):
            if x == rd:
                matrix[x][y] = matrix[x][y] + matrix[rs][y]*m
                
def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     
        grid += [row]

    return grid

def transpose(matrix):
    """gets a matrix and transposes it, in which n*m becomes m*n."""
    height = len(matrix)
    width = len(matrix[0])
    new_matrix = create_grid(width, height)
    for x in range(width):
        for y in range(height):
            new_matrix[x][y] = matrix[y][x]
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
            r = float(input('index of row: '))
            m = float(input('multiplier: '))
            mult_row(matrix, r, m)
        elif choice == 3:
            rs = int(input('index of source row: '))
            rd = int(input('index of destination row: '))
            add_row_into(matrix, rs, rd)
        elif choice == 4:
            rs = int(input('index of source row: '))
            rd = int(input('index of destination row: '))
            m = float(input('Multiplier: '))
            add_mult_row_into(matrix, m, rs, rd)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
