from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1: Point = point1
        self.point2: Point = point2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)


class Window:
    def __init__(self, w: int, h: int):
        self.root_widget: Tk = Tk()
        self.root_widget.title("test")
        self.canvas: Canvas = Canvas(
            self.root_widget,
            bg="white",
            height=h,
            width=w,
        )
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running: bool = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self.canvas, fill_color)
