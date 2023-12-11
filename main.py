from graphics import Window, Line, Point


def main() -> None:
    window: Window = Window(800, 600)
    line: Line = Line(Point(0, 0), Point(400, 300))
    window.draw_line(line)
    window.wait_for_close()


main()
