#The intution is for each column 'n' check in which row the 'Q' fits. perform recursively for each column, checking all the possibilities so use backtracking
#TC - n*n!
#SC - n^2 for the grid
def solveNQueens(n):
    board = [['.']*n for _ in range(n)] #prepare the board with all empty spaces initially
    res = []

    # check only on the left side (upper diagonal, lower diagonal, left columns) of grid if the current position is not conflicting with other queens
    def isSafe(board, row, col):
        currow = row
        curcol = col

        # check for queens on the left upper diagonal
        while(row>=0 and col>=0):
            if board[row][col] == 'Q':
                return False
            row-=1
            col-=1
        
        # check for any queens in the left
        row = currow
        col = curcol
        while(col>=0):
            if board[row][col] == 'Q':
                return False
            col-=1
        
        # check on the left lower diagonal
        row = currow
        col = curcol
        while(col>=0 and row<n):
            if board[row][col] == 'Q':
                return False
            row+=1
            col-=1
        
        return True #return true if there is no conflit
        
    
    def nQueens(col, board):
        # once the col reaches the end record the board to the result, that mean we are done with one complete check and placement of N queens in the grid
        if col == n:
            res.append([''.join(row) for row in board])
            return

        # iterate through the rows of each column for right placement
        for row in range(n):
            # check if current row, col are correct spot to place a 'Q' check all the directions
            if isSafe(board, row, col):
                board[row][col] = 'Q'  #if this position is conflicting with any other queens place 'Q'
                nQueens(col+1, board) #recursion on the next columns, check for all rows in the next columns and so..on
                board[row][col] = '.' #remove 'Q' while backtracking make it empty
    
    nQueens(0, board)
    return res