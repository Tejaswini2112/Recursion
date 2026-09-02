#Approach - Use BFS, first collect all rotten oranges indexes into the queue, 
# for each element in the queue, traverse through the neighbours and if they are fresh turn them into rotten 
# maintain the fresh oranges count while traversing the grid and decrement it every time you turn a fresh orange into rotten one
# TC - O(n*m), SC - (n*m)-> queue can contain all the grid values in the worst case
from collections import deque

def orangesRotting(grid):
    n = len(grid)
    m = len(grid[0])
    queue = deque()
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    time = 0
    fresh = 0
    flag = False

    # loop through the grid values to store the indexes of all rotten oranges and maintain fresh count
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                fresh+=1
            if grid[i][j] == 2:
                queue.append((i,j))

    while(queue):
        size = len(queue)
        flag = False #maintain a flag to record the time only in a pass when atleast one orange is turned rotten
        for i in range(size):
            r, c = queue.popleft()

            for rr, cc in directions:
                nr = r+rr
                nc = c+cc

                if 0<=nr<n and 0<=nc<m and grid[nr][nc] == 1: #check for fresh orange
                    grid[nr][nc] = 2 #turn it into rotten
                    queue.append((nr, nc)) #add the rotten to queue to process in the next pass or time
                    fresh-=1 #fresh count goes down by 1
                    flag = True 
        if flag:
            time+=1 # add to time only when any oranges in the current level are turned rotten

    if fresh!=0:
        return -1
    else:
        return time

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))