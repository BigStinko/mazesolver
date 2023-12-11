from graphics import Window, Line, Point
from cell import Cell


def main() -> None:
    window: Window = Window(800, 600)
    c: Cell = Cell(window)
    c.has_top_wall = False
    c.draw(50, 50, 100, 100)
    window.wait_for_close()


main()
