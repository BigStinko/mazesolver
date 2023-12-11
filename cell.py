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
        self._window: Window = window

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
