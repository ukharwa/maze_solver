from draw import *
from time import sleep
import random

class Maze:
    def __init__(self, start, width, height, rows, cols, window=None, seed=None):
        self.start = start
        self.width = width
        self.height = height

        self.rows = rows
        self.cols = cols    

        self.color = "black"
        self.window = window

        if seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self.cells = []
        cell_width = self.width//self.cols
        cell_height = self.height//self.rows

        for i in range(self.start.y, self.height + cell_height, cell_height):
            row = []
            for j in range(self.start.x, self.width + cell_width, cell_width):
                row.append(Cell(Point(j, i), cell_width, cell_height, self.window))
            self.cells.append(row)
        
        for row in self.cells:
            for cell in row:
                self._draw_cell(cell)
    
    def _draw_cell(self, cell):
        cell.draw(self.color)
        self._animate()

    def _animate(self):
        self.window.redraw()
        sleep(0.03)

    def _break_entrance_exit(self):
        self.cells[0][0].has_top = False
        self.cells[-1][-1].has_bottom = False
        
        self._draw_cell(self.cells[0][0])
        self._draw_cell(self.cells[-1][-1])

    def _break_walls_r(self, i, j):
        cell = self.cells[i][j]
        cell.visited = True
        while True:
            to_visit = []
            if i != 0 and not self.cells[i-1][j].visited:
                to_visit.append([i-1, j, 1])
            if j != 0 and not self.cells[i][j-1].visited:
                to_visit.append([i, j-1, 4])
            if i != self.rows - 1 and not self.cells[i+1][j].visited:
                to_visit.append([i+1, j, 3])
            if j != self.cols - 1 and not self.cells[i][j+1].visited:
                to_visit.append([i, j+1, 2])
            
            if to_visit:
                next = to_visit.pop(random.randint(0, len(to_visit) - 1))
                if next[2] == 1:
                    cell.has_top = False
                    self.cells[next[0]][next[1]].has_bottom = False
                if next[2] == 2:
                    cell.has_right = False
                    self.cells[next[0]][next[1]].has_left = False
                if next[2] == 3:
                    cell.has_bottom = False
                    self.cells[next[0]][next[1]].has_top = False
                if next[2] == 4:
                    cell.has_left = False
                    self.cells[next[0]][next[1]].has_right = False
                self._break_walls_r(next[0], next[1])
            else:
                self._draw_cell(cell)
                return

    def _reset_cells_visited(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False
    
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True
        if i == self.rows - 1 and j == self.cols -1:
            return True

        if i != self.rows - 1 and not self.cells[i+1][j].visited and not current_cell.has_bottom:
            self.cells[i+1][j].draw_move(current_cell)
            if self._solve_r(i+1, j):
                return True
            else:
                self.cells[i+1][j].draw_move(current_cell, True)
        
        if j != self.cols - 1 and not self.cells[i][j+1].visited and not current_cell.has_right:
            self.cells[i][j+1].draw_move(current_cell)
            if self._solve_r(i, j+1):
                return True
            else:
                self.cells[i][j+1].draw_move(current_cell, True)
        
        if i != 0 and not self.cells[i-1][j].visited and not current_cell.has_top:
            self.cells[i-1][j].draw_move(current_cell)
            if self._solve_r(i-1, j):
                return True
            else:
                self.cells[i-1][j].draw_move(current_cell, True)

        if j != 0 and not self.cells[i][j-1].visited and not current_cell.has_left:
            self.cells[i][j-1].draw_move(current_cell)
            if self._solve_r(i, j-1):
                return True
            else:
                self.cells[i][j-1].draw_move(current_cell, True)



        
                
        

    
    def solve(self):
        self._solve_r(0 , 0)