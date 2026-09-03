#Approach- use normal dfs, loop through all the nodes and traverse all the unvisited nodes, if there are no further neighbours to explore add them to a stack/list. if using stack add to res as you pop, if using list just reverse it to get the topological sort
# TC - O(V+E), SC - O(V+E)
def topoSort(V, edges):
    
    visited = set()
    ans = []
    
    def dfs(node, adjList, visited):
        visited.add(node)
        
        for neighbour in adjList[node]:
            if neighbour not in visited:
                dfs(neighbour, adjList, visited)
        
        ans.append(node) #add to the result once done exploring all its neighbours
    
    
    # build the adjacency list
    adjList = [[] for _ in range(V)]
    
    for u,v in edges:
        adjList[u].append(v)
        
    # loop through all the nodes/vertices
    for i in range(V):
        if i not in visited:
            dfs(i, adjList, visited)
    
    ans.reverse() # reverse for topological order
    return ans