# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_deck.ipynb.

# %% auto 0
__all__ = ['Card', 'FrenchDeck']

# %% ../nbs/00_deck.ipynb 2
import random
import collections
from typing import List, Iterator

from fastcore.basics import patch

# %% ../nbs/00_deck.ipynb 5
Card = collections.namedtuple("Card", ["rank", "suit"])

# %% ../nbs/00_deck.ipynb 9
#| code-fold: true
class FrenchDeck:
    ranks = [n for n in range(1, 14)]
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __iter__(self) -> Iterator[Card]:
        return iter(self.cards)

    def __repr__(self):
        return "\n".join(str(card) for card in self.cards)

# %% ../nbs/00_deck.ipynb 18
@patch
def shuffle(self: FrenchDeck) -> FrenchDeck:
    """Shuffles all cards available"""
    random.shuffle(self.cards)

    return self

# %% ../nbs/00_deck.ipynb 19
@patch
def draw(self: FrenchDeck) -> Card:
    """Removes a card from the top of the deck"""
    card = self.cards.pop()

    return card

# %% ../nbs/00_deck.ipynb 22
@patch
# number of cards to draw
def draw_n(self: FrenchDeck, n_cards: int) -> List[Card]:
    """Removes `n` cards from the top of the deck"""
    cards = []

    for i in range(n_cards):
        if len(self) == 0:
            return []

        card = self.draw()  # type: ignore
        cards.append(card)

    return cards