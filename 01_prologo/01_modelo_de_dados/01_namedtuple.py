import collections
from itertools import product
from random import sample

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self) -> None:
        self._cards = [Card(r, s) for r,s in product(self.ranks, self.suits)]
        self.cards = sample(self._cards, len(self._cards))
        
    def __len__(self) -> int:
        return len(self._cards)
    
    def __getitem__(self, position: int) -> Card:
        return self.cards[position]


if __name__ == "__main__":
    deck = FrenchDeck()