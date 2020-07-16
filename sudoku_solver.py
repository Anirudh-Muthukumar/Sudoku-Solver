from collections import defaultdict

class SudokuSolver:
    def __init__(self, board):
        self.board = [x[::] for x in board]
        self.path = []
        mat = [x[::] for x in self.board]
        self.path.append([mat, [0,0]])
        
    
    def findEmptyCell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]==0:
                    return i, j
        return -1, -1

    def canFill(self, x, y, digit):
        row = x-x%3
        col = y-y%3 

        # check if digit in 3 x 3 grid
        for i in range(3):
            for j in range(3):
                if self.board[row+i][col+j]==digit:
                    return False 
        
        # check if digit in row/column
        for k in range(9):
            if self.board[x][k]==digit or self.board[k][y]==digit:
                return False 
        
        # Otherwise can fill the cell
        return True
    
    def solve(self):  
        x, y = self.findEmptyCell()
        if x == -1: # finished solving the puzzle
            return True
        
        for digit in range(1, 10):
            if self.canFill(x, y, digit):
                self.board[x][y] = digit 
                old_matrix = self.path[-1][0]
                new_matrix = [x[::] for x in old_matrix]
                new_matrix[x][y] = digit
                self.path.append([new_matrix, [x, y]])
                if self.solve():
                    return True, self.board, self.path 
                self.board[x][y] = 0 # backtrack 
                old_matrix = self.path[-1][0]
                new_matrix = [x[::] for x in old_matrix]
                new_matrix[x][y] = digit
                self.path.append([new_matrix, [x, y]])
        
        return False


# if __name__ == "__main__":
#     board = [[3,0,6,5,0,8,4,0,0], 
#             [5,2,0,0,0,0,0,0,0], 
#             [0,8,7,0,0,0,0,3,1], 
#             [0,0,3,0,1,0,0,8,0], 
#             [9,0,0,8,6,3,0,0,5], 
#             [0,5,0,0,9,0,6,0,0], 
#             [1,3,0,0,0,0,2,5,0], 
#             [0,0,0,0,0,0,0,7,4], 
#             [0,0,5,2,0,6,3,0,0]] 

#     solver = SudokuSolver(board)
#     result, grid, path = solver.solve()
#     if result:
#         for i in range(9):
#             print(grid[i])
#         print(len(path))
#         for i in range(9):
#             print("Step :" , i+1)
#             for j in range(9):
#                 print(path[i][0][j])
#     else:
#         print("NO")
