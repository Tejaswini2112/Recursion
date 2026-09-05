#Approach - to find the nearest 0's do bfs traversal on all the 0's and at each level if you see a 1 the output should be at which level you are in currently from where you started, the 1's keep adding at every level(its basically the distance from the 0)

from collections import deque


def updateMatrix(mat):
    n = len(mat)
    m = len(mat[0])
    queue = deque()
    visited = set()
    output = [[0]*m for _ in range(n)]
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    # have all the positions of 0's in your queue
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                queue.append((i,j,0)) #row, column and the distance
                visited.add((i,j)) #mark all the 0's visited
            
    
    while(queue):
        r,c,dis = queue.popleft()
        output[r][c] = dis #record the distance of current element in the queue
        for rr,cc in directions:
            nr = rr+r
            nc = c+cc
            # check on all 4 directions for the non visited positions, they are definitely going to be 1's because we already visited all the 0's
            if 0<=nr<n and 0<=nc<m and (nr, nc) not in visited:
                visited.add((nr,nc))
                queue.append((nr,nc,dis+1))

    return output

