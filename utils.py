from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other: Position) -> Position:
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Position) -> Position:
        return Position(self.x - other.x, self.y - other.y)

    def __eq__(self, other: Position) -> bool:
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        yield self.x
        yield self.y

    def is_even(self) -> bool:
        return (self.x + self.y) % 2 == 0
