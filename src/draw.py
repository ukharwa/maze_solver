
from tkinter import Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) +")"


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self, canvas, color):
        canvas.create_line(self.start.x ,self.start.y, self.end.x, self.end.y, fill=color, width=2)


class Cell:
    def __init__(self, start, width, height, window=None):
        self.x = start.x
        self.y = start.y
        self.width = width
        self.height = height
        self.center = Point(self.x + self.width/2 , self.y + self.height/2)

        self.window = window

        self.has_left = True
        self.has_right = True
        self.has_top = True
        self.has_bottom = True

        self.visited = False


    def draw(self, color):
        if self.has_top:
            self.window.draw_line(Line(Point(self.x, self.y), Point(self.x+self.width, self.y)), color)
        else:
            self.window.draw_line(Line(Point(self.x, self.y), Point(self.x+self.width, self.y)), "white")
        if self.has_bottom:
            self.window.draw_line(Line(Point(self.x, self.y + self.height), Point(self.x+self.width, self.y+self.height)), color)
        else:
            self.window.draw_line(Line(Point(self.x, self.y + self.height), Point(self.x+self.width, self.y+self.height)), "white")
        if self.has_left:
            self.window.draw_line(Line(Point(self.x, self.y), Point(self.x, self.y + self.height)), color)
        else:
            self.window.draw_line(Line(Point(self.x, self.y), Point(self.x, self.y + self.height)), "white")
        if self.has_right:
            self.window.draw_line(Line(Point(self.x+self.width, self.y), Point(self.x+self.width, self.y+self.height)), color)
        else:
            self.window.draw_line(Line(Point(self.x+self.width, self.y), Point(self.x+self.width, self.y+self.height)), "white")
    
    def draw_move(self, cell2, undo=False):
        if undo:
            self.window.draw_line(Line(self.center, cell2.center), "gray")
        else:
            self.window.draw_line(Line(self.center, cell2.center), "red")

    def __repr__(self):
        return self.center.__repr__()


