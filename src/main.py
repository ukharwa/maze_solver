from window import Window
from draw import *
from maze import Maze

def main():
    window  = Window(1000, 800)
    
    maze = Maze(Point(35, 35), 700, 700, 55, 55, window, 0)
    maze.solve()

    window.wait_for_close()

if __name__ == "__main__":
    main()