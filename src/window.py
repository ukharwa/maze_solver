from tkinter import Tk, BOTH, Canvas
from draw import Line

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, background="white")
        self.canvas.pack(expand=True, padx=(10, 0), pady=(10, 0))

        self.isRunning = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def close(self):
        self.isRunning = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)
    