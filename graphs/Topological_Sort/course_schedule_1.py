#Approach - Use Kanhs algorithm, create an adjacency list, maintain the indegrees of all the courses, 
# add the courses that are independent or having indegree zero to the queue, process the queue, the queue always contain only the independent courses with 0 indegree
# remove the completed course from the queue, loop through its adjacents to reduce the indegree by 1 as the current course is already completed (reducing prerequisites)
# if its adjacents indegree is also 0 meaning it is not dependent add it to queue and continue, keep counting the completed courses
# once out the queue check if all courses are completed


from collections import deque

def canFinish(numCourses, prerequisites):
    queue = deque()
    adjList = [[] for _ in range(numCourses)]
    indegree = [0 for _ in range(numCourses)]
    # create adjacency list
    for u, v in prerequisites:
        adjList[v]. append(u)
        indegree[u]+=1

    # append all courses with no dependencies into the queue i.e., 0 indegree
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
    
    count = 0 # number of courses completed
    while(queue):
        ele = queue.pop()
        count+=1 # count the completed courses
        
        for adj in adjList[ele]:
            indegree[adj]-=1
            if indegree[adj] == 0:
                queue.append(adj)
    
    return count == numCourses