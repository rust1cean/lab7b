from __future__ import annotations
from typing import Dict, Optional
from cell import Cell
from grid import Grid, InvalidCellPosition
from direction import Direction

KNIGHT_MAX_COUNT_OF_DIRECTIONS: int = 8


class NoWay(Exception):
    pass


class Knight:

    def __init__(self, cell: Cell, grid: Grid):
        self.grid: Grid = grid
        self.way: Way = Way(cell, self.grid)
        self.history_of_way: list[Way] = [self.way]

        self.way.set_position(*cell.position)
        self.grid.mark_cell(*cell.position)

    @property
    def current_branch(self) -> Way | None:
        try:
            return self.history_of_way[-1]
        except IndexError:
            return None

    def step(self):
        if self.current_branch.done is False:
            way = self.current_branch.step()

            if way is not None:
                self.history_of_way.append(way)
                self.grid.mark_cell(*way.cell.position)

                return way

        self.step_back()

    def step_back(self):
        if len(self.history_of_way) > 1:
            last_direction = self.current_branch.direction

            self.grid.unmark_last_cell()
            self.history_of_way.pop()

            self.current_branch.forget_subway(last_direction)
        else:
            raise NoWay

    def is_end_of_way(self) -> bool:
        return len(self.grid.marked_cells) == self.grid.size()


class Way:

    def __init__(self, cell: Cell, grid: Grid, direction: Optional[Direction]=None):
        self.cell: Cell = cell
        self.grid: Grid = grid
        self.direction: Direction | None = direction
        self.subways: Dict[Direction, Way] = {}
        self.directions: Dict[Direction, int] = self.find_and_sort_directions_by_grow()

    @property
    def done(self) -> bool:
        return len(self.directions) == 0

    @staticmethod
    def count_of_available_ways(cell: Cell, grid: Grid) -> int:
        counter = 0

        for direction in Direction.all():
            next_position = cell.position + direction.value
            next_cell = grid.get_cell(*next_position)

            if grid.is_it_available_cell(next_cell):
                counter += 1

        return counter

    def find_and_sort_directions_by_grow(self):
        min_count_of_available_ways = KNIGHT_MAX_COUNT_OF_DIRECTIONS
        directions: Dict[Direction, int] = {}

        for direction in Direction.all():
            next_position = self.cell.position + direction.value
            next_cell = self.grid.get_cell(*next_position)

            if self.grid.is_it_available_cell(next_cell):
                count_of_available_ways = Way.count_of_available_ways(next_cell, self.grid)
                directions[direction] = count_of_available_ways

                if count_of_available_ways < min_count_of_available_ways:
                    min_count_of_available_ways = count_of_available_ways

        return dict(sorted(directions.items(), key=lambda item: item[1]))

    def set_position(self, x: int, y: int) -> self:
        self.cell = self.grid.get_cell(x, y)

        if self.cell is None:
            raise InvalidCellPosition

        return self

    def add(self, direction: Direction, cell: Cell) -> Way:
        self.subways[direction] = Way(cell, self.grid, direction=direction,)
        return self.subways[direction]

    def forget_subway(self, direction: Direction):
        del self.directions[direction]

    def step(self) -> Way | None:
        for direction in self.directions:
            next_position = self.cell.position + direction.value
            next_cell = self.grid.get_cell(*next_position)

            if self.grid.is_it_available_cell(next_cell):
                return self.add(direction, next_cell)
