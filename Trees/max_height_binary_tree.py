# Find the max depth or height of the tree
#Recursion
# TC - O(n), SC - O(n)
from tree_utils import build_tree

def maxDepth(root) :
    if root == None:
        return 0
    # find the height of left tree recursively
    l = maxDepth(root.left)
    # find the height of right tree recursively
    r = maxDepth(root.right)

    # after exploring each node's left and right childs, 
    # return the max height so far of that sub tree, i.e., max(left tree, right tree) + 1(current node's height)
    return 1+max(l,r)

root = build_tree([3,9,20,None,None,15,7])
print(maxDepth(root))