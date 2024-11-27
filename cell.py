from utils import Position


class Cell:

    def __init__(self, cell_id: int, x: int, y: int):
        self.id = cell_id
        self.position = Position(x, y)
