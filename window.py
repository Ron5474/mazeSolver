from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title = 'Maze Solver'
        self.canvas = Canvas(self.root_widget, width=self.width, height=self.height)
        self.canvas.pack()
        self.window_is_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self) -> None:
        self.root_widget.update_idletasks()
        self.root_widget.update()
    
    def wait_for_close(self) -> None:
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()

    def close(self) -> None:
        self.window_is_running = False
    
    def draw_line(self, line, fill_color="black") -> None:
        line.draw(self.canvas, fill_color)