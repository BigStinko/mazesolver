from cell import Cell
from graphics import Window
import random
import time


class Maze:
    def __init__(
        self,
        x1: int, y1: int,
        num_rows: int, num_cols: int,
        cell_size_x: int, cell_size_y: int,
        window: Window = None,
        seed=None,
    ):
        self._cells: list = []
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._window: Window = window

        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_walls_r(0, 0)
        self._draw_maze()

    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._window))
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_maze()

    def _draw_maze(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        if self._window is None:
            return
        x1: int = self._x1 + i * self._cell_size_x
        y1: int = self._y1 + j * self._cell_size_y
        x2: int = x1 + self._cell_size_x
        y2: int = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.05)

    def _break_walls_r(self, i: int, j: int):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            direction: int = random.randrange(len(next_index_list))
            next_index = next_index_list[direction]
            self._break_wall(i, j, next_index[0], next_index[1])
            self._break_walls_r(next_index[0], next_index[1])

    def _break_wall(self, i: int, j: int, adjx: int, adjy: int):
        if adjx == i + 1:
            self._cells[i][j].has_right_wall = False
            self._cells[adjx][j].has_left_wall = False
        if adjx == i - 1:
            self._cells[i][j].has_left_wall = False
            self._cells[adjx][j].has_right_wall = False
        if adjy == j + 1:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][adjy].has_top_wall = False
        if adjy == j - 1:
            self._cells[i][j].has_top_wall = False
            self._cells[i][adjy].has_bottom_wall = False

    def _reset_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
