from typing import Optional, Dict
from cell import Cell


class InvalidCellPosition(Exception):
    pass


class Grid:

    def __init__(self, width: int=8, height: int=8):
        self.width: int = width
        self.height: int = height
        self.grid: list[list[Cell]] = []
        self._marked_cells: Dict[int, int] = {}

        self.create_grid()

    @property
    def marked_cells(self) -> list[int]:
        return self._marked_cells.keys()

    def size(self):
        return self.width * self.height

    def rows(self) -> int:
        return round(self.size() / self.width)

    def cols(self) -> int:
        return round(self.size() / self.height)

    @staticmethod
    def id_from_position(x: int, y: int) -> int:
        return x + ((y - 1) * 10)

    def is_it_available_cell(self, cell: Cell) -> bool:
        return cell is not None and cell.id not in self.marked_cells

    # Creates a two-dimensional array of width `self.width` and height `self.height` with indexed fields.
    #
    # Example of 3x3 grid:
    # [
    # [1, 2, 3],
    # [4, 5, 6]
    # [7, 8, 9]
    # ]
    def create_grid(self):
        self.grid = [
            [Cell(Grid.id_from_position(x, y), x, y) for x in range(1, self.width + 1)]
            for y in range(1, self.height + 1)
        ]

    def get_cell(self, x: int, y: int) -> Optional[Cell]:
        try:
            x -= 1
            y -= 1

            if x < 0 or y < 0:
                return None

            return self.grid[y][x]
        except IndexError:
            return None

    def mark_cell(self, x: int, y: int):
        cell = self.get_cell(x, y)

        if cell is not None:
            self._marked_cells[cell.id] = len(self.marked_cells) + 1

    def unmark_last_cell(self):
        self._marked_cells.popitem()

    def print(self):
        result = ""
        format_number = lambda s, max_padding = len(str(self.size())): s + (
            " " * (max_padding - len(s))
        )
        for y, row in enumerate(self.grid):
            row_position = format_number(str(y + 1))
            result += f"{row_position}: "
            for cell in row:
                is_checked: bool = cell.id in self.marked_cells
                checked: str = format_number(str(self._marked_cells[cell.id]) if is_checked else "")
                result += f"{'O' if is_checked else 'X'} ({checked}) "
            result += "\n"

        # result += f"Last step: {self.last_checked}"

        print(result)
