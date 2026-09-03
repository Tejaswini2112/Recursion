# Approach - similar to course schedule 1 but with the result array
# TC, SC - O(V+E)
from collections import deque

def findOrder(numCourses, prerequisites):
    queue = deque()
    adjList = [[] for _ in range(numCourses)]
    indegree = [0 for _ in range(numCourses)]
    res = []
    # create adjacency list
    for u, v in prerequisites:
        adjList[v]. append(u)
        indegree[u]+=1

    # append all courses with no dependencies into the queue i.e., 0 indegree
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
    
    while(queue):
        ele = queue.pop()
        res.append(ele) # add the completed courses
        
        for adj in adjList[ele]:
            indegree[adj]-=1
            if indegree[adj] == 0:
                queue.append(adj)
    
    if len(res) == numCourses: # return the result only if all the courses are completed
        return res
    else:
        return []