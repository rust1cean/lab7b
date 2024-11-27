from __future__ import annotations
from enum import Enum
from cell import Position

KNIGHT_STEP: int = 1
KNIGHT_DOUBLE_STEP: int = 2


class Direction(Enum):
    # Right top
    RRT = Position(
        x=KNIGHT_DOUBLE_STEP,
        y=KNIGHT_STEP,
    )
    RTT = Position(
        x=KNIGHT_STEP,
        y=KNIGHT_DOUBLE_STEP,
    )

    # Left top
    LTT = Position(
        x=-KNIGHT_STEP,
        y=KNIGHT_DOUBLE_STEP,
    )
    LLT = Position(
        x=-KNIGHT_DOUBLE_STEP,
        y=KNIGHT_STEP,
    )

    # Left bottom
    LLB = Position(
        x=-KNIGHT_DOUBLE_STEP,
        y=-KNIGHT_STEP,
    )
    LBB = Position(
        x=-KNIGHT_STEP,
        y=-KNIGHT_DOUBLE_STEP,
    )

    # Right bottom
    RBB = Position(
        x=KNIGHT_DOUBLE_STEP,
        y=-KNIGHT_STEP,
    )
    RRB = Position(
        x=KNIGHT_STEP,
        y=-KNIGHT_DOUBLE_STEP,
    )

    @staticmethod
    def all() -> list[Direction]:
        return [
            Direction.RRT,
            Direction.RTT,
            Direction.LLT,
            Direction.RBB,
            Direction.RRB,
            Direction.LTT,
            Direction.LLB,
            Direction.LBB,
        ]
