#Technique - BFS, explore level by level
#TC - O(n)
#SC - O(n) - width of the tree (queue space) at one time only one level of the tree are in the queue
from tree_utils import build_tree
from collections import deque


def levelOrder(root):
    res = []
    if root == None:
        return []
    
    queue = deque()
    queue.append(root)
    # process each element in the queue until the queue is not empty
    while queue:
        level = [] #to store the current level elements
        size = len(queue) #important to calc the size before looping as using directly may modify the length as we pop
        # loop through all the element in the queue(at one time only elements of one level are stored in the queue)
        for i in range(size):
            node = queue.popleft() #pop the element to process
            level.append(node.val) #record it
            #check if it has left and right elements, if it does add them to the queue for the later processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    
    return res

root = build_tree([3, 9, 20, None, None, 15, 7])
print(levelOrder(root))