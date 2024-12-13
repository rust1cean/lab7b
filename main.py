import os
import traceback
from grid import Grid
from config import Config
from knight import Knight, NoWay

if __name__ == "__main__":
    input_file = open("input.txt")

    try:
        width, height, x, y = Config.parse(input_file)
        grid = Grid(width, height)
        cell = grid.get_cell(x, y)

        if cell is not None:
            knight = Knight(cell, grid)
            while !knight.is_end_of_way():
                knight.step()
                os.system("cls")
                grid.print()

    except NoWay:
        print("Can't find path.")

    except Exception:
        print(traceback.format_exc())

    finally:
        input_file.close()
