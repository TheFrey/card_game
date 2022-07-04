from Const import SUITS, RANKS
from itertools import product
import random


class Card:
    def __init__(self, suit, rank, points, picture=0):
        self.suit = suit
        self.rank = rank
        self.picture = picture
        self.points = points

    def __str__(self):
        return f'{self.suit}, {self.rank}'


class Deck:
    def __init__(self):
        self.cards = self._create_deck()
        random.shuffle(self.cards)

    def _create_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            points = 0
            if rank in ['2', '3', '4', '5', '6', '7', '8', '9']:
                points = int(rank)
            elif rank in ['10', 'jack', 'queen', 'king']:
                points = 10
            elif rank == 'ace':
                points = 11
            card = Card(suit=suit, rank=rank, points=points)
            cards.append(card)
        return cards

    def get_card(self):
        return self.cards.pop()
