from flask import Flask, render_template, url_for, request
from sudoku_solver import SudokuSolver

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', solution = False, result = None, content = None)

@app.route('/clear')
def clear():
    return render_template('index.html', solution = False, result = None, content = None)


@app.route('/solve')
def solve_puzzle():
    cells = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if request.args[str(i)+str(j)]:
                cells[i][j] = int(request.args[str(i)+str(j)])
    
    solver = SudokuSolver(cells)
    result, grid, path = solver.solve()
    return render_template('index.html', solution = True, result = result, content=path)



if __name__ == "__main__":
    app.run()