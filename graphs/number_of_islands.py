# Approach - loop through each node of the grid, if it is a land and not visited, traverse that node using dfs/bfs
# check all the four directions of the node while traversing(left, right, up, down), if you find a land that is not visited traverse it
# TC - O(n*m), SC - O(n*m)

def numIslands(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0
    directions = [(0,1), (0,-1), (1,0), (-1, 0)] #all four directions, left, right, down, up
    visited = set() #(r,c)

    def dfs(r, c, grid):
        # mark visited once you start traversing
        visited.add((r,c))

        #check all 4 directions
        for rr, cc in directions:
            nr = r+rr
            nc = c+cc

            # check for the boundaries and if the new position is a land and not visited to traverse further
            if (nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc] == '1' and (nr,nc) not in visited):
                dfs(nr, nc, grid)

    # loop throughout the grid
    for i in range(n):
        for j in range(m):
            if (i,j) not in visited and grid[i][j] == '1':
                count+=1 #count whenever you are visiting a new node or a not traversed node
                dfs(i,j,grid)

    return count

print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))