# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_hand.ipynb.

# %% auto 0
__all__ = ['Hand']

# %% ../nbs/06_hand.ipynb 2
from nbdev import nbdev_export
from typing import Optional, List, Iterator

from fastcore.basics import patch
from mydeck.core import Card

# %% ../nbs/06_hand.ipynb 3
# | code-fold: true
class Hand:
    def __init__(
        self, max_cards: Optional[int] = None  # Max amount of cards it can be hold
    ):
        self._max_cards = max_cards
        self.cards: List[Card] = []

    def __getitem__(self, value: int):
        return self.cards[value]

    def __len__(self):
        return len(self.cards)

    def __iter__(self) -> Iterator[Card]:
        return iter(self.cards)

    def __repr__(self):
        return "\n".join(str(card) for card in self.cards)

# %% ../nbs/06_hand.ipynb 4
@patch
def draw(self: Hand, card: Card):
    if self._max_cards is None or self._max_cards < len(self.cards):
        self.cards.append(card)
    return self

# %% ../nbs/06_hand.ipynb 5
@patch
def discard(self: Hand, index: int = 0) -> Optional[Card]:
    if index < len(self.cards):
        card = self.cards.pop(index)
        return card

    return None

# %% ../nbs/06_hand.ipynb 6
@patch
def value(self: Hand) -> int:
    return sum([card.rank for card in self])
