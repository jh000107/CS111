#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """ takes two parameters: a Player object for the player whose move
        is being processed, and a Board object for the game that is being played
    """
    print('Player ' + player.checker + "'s turn")
    move = player.next_move(board)
    board.add_checker(player.checker, move)
    print('\n')
    print(board)
    print('\n')
    if board.is_win_for(player.checker) == True:
        print('Player ' + player.checker + ' wins in ' + str(player.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    elif board.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    """ can be used for an unintelligent computer player that chooses at random
        from the available columns
        - a subclass of a superclass Player
    """
    def next_move(self, board):
        """ choose at roandom from the columns in the specified board that are not
            yet full, and return the index of that randomly selected column
        """
        open_columns = []
        for col in range(board.width):
            if board.can_add_to(col) == True:
                open_columns += [col]
        if len(open_columns) > 0:
            self.num_moves += 1
        return random.choice(open_columns)

    
    
    
