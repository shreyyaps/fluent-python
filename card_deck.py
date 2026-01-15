import collections
import random
Card = collections.namedtuple('Cards',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._card)
    
    def __getitem__(self, position):
        return self._card[position]
    



deck = FrenchDeck()

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def order_by(card):
    rank_index = FrenchDeck.ranks.index(card.rank)
    return rank_index * 4 + suit_values.get(card.suit) # type: ignore

for card in sorted(deck, key=order_by):
    print(card)