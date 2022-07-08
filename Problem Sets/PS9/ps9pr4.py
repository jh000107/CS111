#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ a class for an AI player. It uses techniques from artificial intelligence
        to choose its next move
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs an AI player object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer obect """
        s = super().__repr__() + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board and
            returns the index of the column with the maximum score
        """
        max_score = max(scores)
        max_index = []
        for x in range(len(scores)):
            if scores[x] == max_score:
                max_index += [x]
        if self.tiebreak == 'LEFT':
            return max_index[0]
        elif self.tiebreak == 'RIGHT':
            return max_index[-1]
        else:
            return random.choice(max_index)

    def scores_for(self, board):
        """ takes a Board object board and determines the called AIPlayer's
            scores for the columns in board
        """
        scores = [0] * board.width
        for column in range(board.width):
            if board.can_add_to(column) == False:
                scores[column] = -1
            elif board.is_win_for(self.checker):
                scores[column] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[column] = 0
            else:
                if self.lookahead == 0:
                    scores[column] = 50
                else:
                    board.add_checker(self.checker, column)
                    opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                    opponent_score = opponent.scores_for(board)
                    if max(opponent_score) == 100:
                        scores[column] = 0
                    elif max(opponent_score) == 0:
                        scores[column] = 100
                    else:
                        scores[column] = 50
                    board.remove_checker(column)
        return scores

    def next_move(self, board):
        """ return the called AIPlayer's judgment of its best possible move
        """
        index = self.max_score_column(self.scores_for(board))
        self.num_moves += 1
        return index

    
                    
                    
                    
            
