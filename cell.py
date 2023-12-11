from graphics import Window, Line, Point


class Cell:
    def __init__(self, window: Window):
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self._x1: int = 0
        self._y1: int = 0
        self._x2: int = 0
        self._y2: int = 0
        self.visited: bool = False
        self._window: Window = window

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

    # draws a line to a directly adjacent cell. (up, down, left, right)
    def draw_move(self, to_cell, undo: bool = False):
        if self._window is None:
            return
        x_mid: int = (self._x1 + self._x2) // 2
        y_mid: int = (self._y1 + self._y2) // 2

        to_x_mid: int = (to_cell._x1 + to_cell._x2) // 2
        to_y_mid: int = (to_cell._y1 + to_cell._y2) // 2

        fill_color: str = "red"
        if undo:
            fill_color = "gray"

        if self._x1 > to_cell._x1:  # to_cell is to the right
            self._window.draw_line(
                Line(Point(self._x1, y_mid), Point(x_mid, y_mid)),
                fill_color,
            )
            self._window.draw_line(
                Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid)),
                fill_color,
            )
        elif self._x1 < to_cell._x1:  # to_cell is to the left
            self._window.draw_line(
                Line(Point(x_mid, y_mid), Point(self._x2, y_mid)),
                fill_color,
            )
            self._window.draw_line(
                Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid)),
                fill_color,
            )
        elif self._y1 > to_cell._y1:  # to_cell is above
            self._window.draw_line(
                Line(Point(x_mid, y_mid), Point(x_mid, self._y1)),
                fill_color,
            )
            self._window.draw_line(
                Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid)),
                fill_color,
            )
        elif self._y1 < to_cell._y1:  # to_cell is below
            self._window.draw_line(
                Line(Point(x_mid, y_mid), Point(x_mid, self._y2)),
                fill_color,
            )
            self._window.draw_line(
                Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1)),
                fill_color,
            )
