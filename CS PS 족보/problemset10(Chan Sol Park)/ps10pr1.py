# Chan Sol Park
# chansol@bu.edu
# Ps10pr1 A Connect Four Board Class
# Partner: Dohyung Kim, pk@bu.edu

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """
    def __init__(self, height, width):
        """ constructs a new Board object by initializing"""
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ returns a string representing a Board object"""
        s = ''         
        for row in range(self.height):
            s = s + '|'   
            for col in range(self.width):
                s = s + self.slots[row][col] + '|'
            s += '\n'
        x = 2*self.width+1
        s = s + ('-'*x)
        s = s +'\n'    
        for col in range(self.width):
            s = s + ' '+ str(col%10)
        return s

    def add_checker(self, checker, col):
        """ adds the specific checker to column of the Board """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row = row + 1
        self.slots[row-1][col] = checker

    def reset(self):
        """resets the Board object on which it is called by setting
           all slots to contain a space character
        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] =" "


    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """returns True if it is valid to place a checker in the
           column col on the calling Board object. Otherwise, it
           returns False
        """
        if col >= 0 and col < self.width:
            if self.slots[0][col] == ' ':
                return True
            else:
                return False
        else:
            return False

    def is_full(self):
        """returns True if the called Board object is completely full
           of checkers, and returns False otherwise
        """
        for r in range(self.height):
            for c in range(self.width):
                if self.slots[r][c]==' ':
                    return False
        return True


    def remove_checker(self, col):
        """removes the top checker from column col of the called Board
           object. If the column is empty, then the method should do nothing.
        """
        row = 0
        while row < self.height-1 and self.slots[row][col] == ' ':
            row += 1
        self.slots[row][col] = ' '

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        return False
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True

        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                self.slots[row+1][col+1] == checker and \
                self.slots[row+2][col+2] == checker and \
                self.slots[row+3][col+3] == checker:
                 return True

        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                self.slots[row-1][col+1] == checker and \
                self.slots[row-2][col+2] == checker and \
                self.slots[row-3][col+3] == checker:
                 return True

        return False


    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots
            containing checker on the board
        """
        assert(checker == 'X' or checker == 'O')

        vertical= self.is_vertical_win(checker)
        horizontal=self.is_horizontal_win(checker)
        down=self.is_down_diagonal_win(checker)
        up=self.is_up_diagonal_win(checker)

        return vertical or horizontal or down or up
    

       
            


    

        

