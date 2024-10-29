from window import Window
from draw import *
from maze import Maze

def main():
    window  = Window(600, 600)
    
    maze = Maze(Point(50, 50), 500, 500, 10, 10, window)
    maze.solve()

    window.wait_for_close()

if __name__ == "__main__":
    main()