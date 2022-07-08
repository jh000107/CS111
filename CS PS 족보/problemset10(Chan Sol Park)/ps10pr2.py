#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#

from ps10pr1 import Board

# write your class below

class Player:
            """a data type for a player"""
            
            def __init__(self, checker):
                        """constructs a new Player object"""
                        self.checker = checker
                        self.num_moves = 0
                        
            def __repr__(self):
                        """returns a string representing a Player object"""
                        if self.checker == 'X':
                                    s =  'Player X'
                        elif self.checker == 'O':
                                    s = 'Player O'
                        else:
                                    False
                        return s
            
            def opponent_checker(self):
                        """returns a one-character string representing the
                           checker of the Player object’s opponent
                        """
                        if self.checker == 'O':
                                    b =  'X'
                        elif self.checker == 'X':
                                    b = 'O'
                        return b
            
            def next_move(self, board):
                        """ returns the column where the player wants to make
                            the next move
                        """
                        while True:
                                    column = int(eval(input('Enter a column: ')))
                                    if board.can_add_to(column) == True:
                                                self.num_moves += 1
                                                return column
                                    else:
                                                print('Try again!')
