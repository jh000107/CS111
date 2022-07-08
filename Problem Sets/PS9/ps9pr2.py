#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below
class Player:
    """ a Player class to represent a player of the Connect Four game """
    
    def __init__(self, checker):
        """ constructs a new Player object by initializing the following two
            attributes:
            chekcer is a one-character string that represents the gamepiece
            for the player
            num_moves is an integer that stores how many moves the player has
            made so far
        """
        assert(checker == 'O' or checker == 'X')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing a Player object.
        """
        s = 'Player '
        s += self.checker
        return s

    def opponent_checker(self):
        """ returns a one-character string representing the checker of the
            Player object's opponent.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """ returns the column where the player wants to make the next move
            input: a Board object
        """
        while True:
            column = int(input('Enter a column: '))
            if board.can_add_to(column) == True:
                self.num_moves += 1
                return column
            else:
                print('Try again')
        

    
    
