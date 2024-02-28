def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end="")
        print("")

def position(row, column, inputP, maze, checkWin):
    if inputP == "W" and maze[row-1][column] != "X":
        if maze[row-1][column] == '*':
            checkWin = True
        maze[row-1][column] = 'P'
        maze[row][column] = '.'
        return row - 1, column, checkWin
    if inputP == "S" and maze[row+1][column] != "X":
        if maze[row+1][column] == '*':
            checkWin = True
        maze[row+1][column] = 'P'
        maze[row][column] = '.'
        return row + 1, column, checkWin
    if inputP == "A" and maze[row][column-1] != "X":
        if maze[row][column-1] == '*':
            checkWin = True
        maze[row][column-1] = 'P'
        maze[row][column] = '.'
        return row, column - 1, checkWin
    if inputP == "D" and maze[row][column+1] != "X":
        if maze[row][column+1] == '*':
            checkWin = True
        maze[row][column+1] = 'P'
        maze[row][column] = '.'
        return row, column + 1, checkWin
    return row, column, checkWin

maze = [
    ['X', '*', 'X', 'X', 'X'],
    ['X', '.', '.', '.', 'X'],
    ['X', 'X', 'X', '.', 'X'],
    ['X', '.', '.', '.', 'X'],
    ['X', 'P', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', 'X']
]
row = 4
column = 1 
checkWin = False
while True:
    print_maze(maze)
    inputP = input("Enter W, A, S, D to move (or Q to quit): ")
    
    if inputP == 'Q':
        break

    row, column, checkWin = position(row, column, inputP, maze, checkWin)
    
    if checkWin:
        print("Congratulations! You won!")
        break
