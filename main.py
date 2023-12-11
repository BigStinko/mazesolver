from graphics import Window
from maze import Maze


def main() -> None:
    num_rows: int = 12
    num_cols: int = 16
    margin: int = 50
    screen_width: int = 800
    screen_height: int = 600
    cell_size_x: int = (screen_width - 2 * margin) // num_cols
    cell_size_y: int = (screen_height - 2 * margin) // num_rows
    window: Window = Window(screen_width, screen_height)

    maze: Maze = Maze(
        margin, margin,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        window
    )

    window.wait_for_close()


main()
