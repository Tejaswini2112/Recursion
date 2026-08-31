#Approach - At each level only one value, i.e., the right most value at every level should be added to the result
#follow reverse preorder (ele, right, left) traverse on the right tree first then left tree
#at each level append the first element you see from the right
# TC - O(n), SC - O(h)
from tree_utils import build_tree

def rightSideView(root):
    res = []
    def treeView(root, level):
        if not root:
            return None

        # res has only 1 ele per level, so its length at entering every level is same as the level, that means we found the first right element on this level so just append
        if level == len(res):
            res.append(root.val)

        # right traversal first then left
        treeView(root.right, level+1)
        treeView(root.left, level+1)

    
    treeView(root, 0)
    return res

root = build_tree([1,2,3,4,None,None,None,5])
print(rightSideView(root))