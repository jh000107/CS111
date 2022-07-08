#
# hand.py
#
# CS 111, Boston University
#

from card import *

class Hand:
    """ a class for objects that represent a single hand of cards """

    def __init__(self):
        """ constructor for Hand objects """
        self.cards = []

    def __repr__(self):
        """ returns a string representation of the called Hand object (self) """
        return str(self.cards)

    def add_card(self, card):
        """ add the specified Card object (card) to the list of cards
            for the called Hand object (self)
        """
        self.cards += [card]

    def num_cards(self):
        """ returns the number of cards in the called Hand obejct(self)
        """
        return len(self.cards)

    def get_value(self):
        """ returns the total value of the cards in the called Hand object
        """
        total = 0
        for x in self.cards:
            total += x.get_value()
        return total
