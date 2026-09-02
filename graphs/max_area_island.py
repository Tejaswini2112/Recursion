#Approach - to find the maximum area, first traverse through all the islands by checking all four directions for 1's using DFS, 
# while traversing calculate the area, every traversal will add up to the area, calculate the max area of all the islands
#TC - O(n*m), SC - O(n*m)

def maxAreaOfIsland(grid):
    n = len(grid)
    m = len(grid[0])
    visited = set()
    max_area = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(r, c):
        visited.add((r,c))
        area = 1 # area of the traversed node
        for rr, cc in directions:
            nr = r+rr
            nc = c+cc

            if 0<=nr<n and 0<=nc<m and grid[nr][nc] == 1 and (nr,nc) not in visited:
                area+=dfs(nr, nc) #add up to the total area
        return area

        
    for i in range(n):
        for j in range(m):
            if (i,j) not in visited and grid[i][j] == 1:
                max_area = max(max_area, dfs(i,j)) # get the max area

    return max_area