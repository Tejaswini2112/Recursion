# Approach - using kahns algorithm to get the topological sort(linear order of the graph) for a graph
# get all the indegrees for all the nodes
# collect all the nodes having zero indegree into a queue(that means they are not dependent, so they go first and later its neighbours that are dependent on these nodes will be explored)
# pop from the queue and check its neighbours and reduce the indegree of its neighbours as we have already processed this node
# if the indegree of it neighbour becomes zero add it to the queue, keep continuing till the queue is not empty
# TC, SC - O(V+E)

from collections import deque

def kahns_algorithm(V, edges):
    
    indegree = [0 for _ in range(V)]
    queue = deque()
    ans=[]
    
    # build the adjacency list
    adjList = [[] for _ in range(V)]

    # calculate indegree for each node
    for u,v in edges:
        adjList[u].append(v)
        indegree[v]+=1

    # append all node with indegree 0 to the queue
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)
    
    while(queue):
        
        ele = queue.pop()
        ans.append(ele)
        
        for adj in adjList[ele]:
            indegree[adj]-=1 #decrement the indegree of adjacent node
            if indegree[adj] == 0:
                queue.append(adj)
    # cycle detection, if the result length is not equal to the length of the nodes that means theres a cycle           
    if len(ans) != V:
        return [] 
    return ans