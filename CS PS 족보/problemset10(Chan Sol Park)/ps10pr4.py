#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four
#

import random  
from ps10pr3 import *

class AIPlayer(Player):
            """Creates an AI player for the connect four game program"""
            def __init__(self, checker, tiebreak, lookahead):
                        """ put your docstring here
                        """
                        assert(checker == 'X' or checker == 'O')
                        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
                        assert(lookahead >= 0)
                        self.checker = checker
                        self.tiebreak = tiebreak
                        self.lookahead = lookahead
                        super().__init__(checker)

            def __repr__(self):
                        """returns a string representing an AIPlayer object"""
                        if self.checker == 'X':
                                    s =  'Player X' +' ('+str(self.tiebreak)+', '+str(self.lookahead)+')'
                        elif self.checker == 'O':
                                    s = 'Player O' +' ('+str(self.tiebreak)+', '+str(self.lookahead)+')'
                        else:
                                    False
                        return s
            def max_score_column(self, scores):
                        """takes a list scores containing a score for each
                           column of the board, and that returns the index
                           of the column with the maximum score
                        """
                        maxes = []
                        value = max(scores)
                        for r in range(len(scores)):
                                    if scores[r] == value:
                                                maxes+= [r]
                                    
                        if self.tiebreak == 'LEFT':
                                    return maxes[0]
                                    
                        elif self.tiebreak == 'RIGHT':
                                    return maxes[-1]
                        else:
                                    return random.choice(maxes)
                        
            def scores_for(self, board):
                        """ takes a Board object board and determines the called
                            AIPlayer‘s scores for the columns in board.  takes a
                            Board object board and determines the called AIPlayer's
                            scores for the columns in board
                        """
                        scores = [50]*board.width
                        for col in range(board.width):
                            if board.can_add_to(col) == False:
                                scores[col] = -1
                            elif board.is_win_for(self.checker) == True:
                                scores[col] = 100
                            elif board.is_win_for(self.opponent_checker()) == True:
                                scores[col] = 0
                            elif self.lookahead == 0:
                                scores[col] = 50
                            else:
                                board.add_checker(self.checker, col)
                                opponent = AIPlayer(self.opponent_checker(), self.tiebreak,self.lookahead-1)
                                opp_scores = opponent.scores_for(board)
                                if max(opp_scores) == 0:
                                    scores[col] = 100
                                elif max(opp_scores) == 100:
                                    scores[col] = 0
                                else:
                                    scores[col] = 50
                                board.remove_checker(col)
                        return scores

            def next_move(self, board):
                """return the called AIPlayer‘s judgment of its best possible move"""
                value = self.max_score_column(self.scores_for(board))
                self.num_moves += 1
                return value
                
                
                
                    
                    

            
