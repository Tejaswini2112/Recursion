#Approach - for each node in the main tree compare it with the subRoot tree(using isSameTree function), if the trees are equal it means the main tree has the sub tree in it
#TC - O(n*m) - (no.of nodes main tree and no.of nodes of sub tree)
#SC - O(n+m)
from tree_utils import build_tree

def isSubtree(root, subRoot):
    # compare to check if two trees are same (p tre, q tree)
    def isSameTree(p, q):
        if not p and not q: # if both reached the bottom or are empty return true
            return True
        if not p or not q: #if one tree is empty and the other is not empty, they are not same return false
            return False
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right) # compare the values of two trees and recurse on left and right sub trees, all should return true only then the trees are same 

    # walk through the entire tree recursively to check for each node if is the sub tree needed
    def checkSubTree(root, subRoot):
        if root == None:
            return False
        l = checkSubTree(root.left, subRoot)
        r = checkSubTree(root.right, subRoot)
        return isSameTree(root, subRoot) or l or r 
    return checkSubTree(root, subRoot)


root = build_tree([3,4,5,1,2])
subRoot = build_tree([4,1,2])
print(isSubtree(root, subRoot))

