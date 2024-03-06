import collections
from itertools import product
from random import sample, shuffle

class ExtractionException(Exception):
    def __init__(self, message="Extraction failed", errors=None) -> None:
        super().__init__(message)
        self.errors = errors

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    _ranks = [str(n) for n in range(2,11)] + list('JQKA')
    _suits = 'spades diamonds clubs hearts'.split()
    _cards = [Card(r, s) for r,s in product(_ranks, _suits)]
    
    def __init__(self) -> None:
        self.cards = sample(self._cards, len(self._cards))
        
    def __len__(self) -> int:
        return len(self.cards)
    
    def __getitem__(self, position: int) -> Card:
        return self.cards[position]

    def __repr__(self) -> str:
        _s = ""
        acc = 0
        for c in self.cards:
            if acc % 5 == 0: _s += '\n'
            else: _s += '\t'
            _s += c.rank + c.suit[0]
            acc+=1
        _s += '\n'
        return _s

    def __bool__(self) -> bool:
        """ Answers the question 'is this deck original'?
        """
        if len(self) == len(self._cards): return True
        return False

    def shuffle(self):
        """
        Shuffles the cards in the deck.
        """
        shuffle(self.cards)

    def pick(self, number_of_cards: int = 1) -> list[Card]:
        """
        Picks a specified number of cards from the deck.

        Args:
            number_of_cards (int): The number of cards to pick from the deck. Defaults to 1.

        Returns:
            list[Card]: A list of picked cards.
        """
        extractions: list[Card] = []
        if len(self) < number_of_cards:
            raise ExtractionException(f"Tried to extract {number_of_cards} cards, but there are only {len(self)} cards remaining.")
        
        for _ in range(number_of_cards):
            extractions.append(self.cards.pop())
        return extractions

if __name__ == "__main__":
    deck = FrenchDeck()