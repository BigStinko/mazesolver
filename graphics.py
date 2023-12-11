from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, w: int, h: int):
        self.root_widget: Tk = Tk()
        self.root_widget.title("test")
        self.canvas: Canvas = Canvas(
            self.root_widget,
            bg="black",
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
