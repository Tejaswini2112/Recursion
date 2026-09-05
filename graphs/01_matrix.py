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
                queue.append((i,j,0))
                visited.add((i,j))
            
    
    while(queue):
        r,c,dis = queue.popleft()
        output[r][c] = dis
        for rr,cc in directions:
            nr = rr+r
            nc = c+cc
            if 0<=nr<n and 0<=nc<m and (nr, nc) not in visited:
                visited.add((nr,nc))
                queue.append((nr,nc,dis+1))

    return output

