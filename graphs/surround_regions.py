#Approach - Mark all Os connected to the boundary using DFS and temporarily change them to -1 (safe).
# Then scan the board: change remaining Os to X, and change -1 back to O.
# TC - O(n*m), SC-O(n*m)
def solve(board):
    n = len(board)
    m = len(board[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    def dfs(r,c):
        board[r][c] = -1 #mark the visited node as -1 that means they remain O

        for rr,cc in directions:
            nr = r+rr
            nc = c+cc

            if 0<=nr<n and 0<=nc<m and board[nr][nc] == 'O':
                dfs(nr,nc)

    # loop through the column and last cloumn to check for O's (boundaries)
    for i in range(n):
        if board[i][0] == 'O':
            dfs(i,0)
        if board[i][m-1] == 'O':
            dfs(i, m-1)

    # check for O's in the 1st and last rows
    for j in range(m):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[n-1][j] == 'O':
            dfs(n-1, j)

    # mark the -1 back to O's and O's to X
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'
    print(board)