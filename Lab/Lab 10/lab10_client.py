#
# lab10_client.py
#
# CS 111, Boston University
#

from card import *
from hand import *

c1 = Card(7, 'H')
c2 = Card('A', 'D')

h1 = Hand()
h1.add_card(c1)
h1.add_card(c2)
print('first hand:', h1)

print('number of cards:', h1.num_cards())

print('total value:', h1.get_value())
