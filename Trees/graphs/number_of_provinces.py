#Approach - convert the matrix into an adjacency list, loop through the nodes and traverse each node and mark the visited once, once there is a break calculate the count
#TC - O(n^2) - for looping to create the adjlist, if adjlist is already given then it should be O(V+2E) - Every node is visited once → O(V), Every edge is examined once (or twice for an undirected graph) → O(E)
#SC - O(n) - for visited set + adjlist
def findCircleNum(isConnected):
    n = len(isConnected)
    adjList = [[] for _ in range(n)]
    visited = set()
    count = 0

    # dfs traversal on each node
    def dfs(num):
        visited.add(num)
        for it in adjList[num]: #loop through the neighbours or adjacent nodes
            if it not in visited: #traverse them only if they are not visited
                dfs(it)

    # create adjacency list
    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1 and i!=j:
                adjList[i].append(j)

    # loop through all the nodes to check if they are visited, if not traverse using dfs
    for i in range(n):
        if i not in visited: # if this node is not visited means it is a different province so add to the count
            count+=1
            dfs(i)
    
    return count

print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
