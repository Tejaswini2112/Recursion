#Approach - find the heights of left and right sub trees for each node, adding both heights would give the max width or diameter
#TC - O(n), SC - O(n)
from tree_utils import build_tree
diameter = 0
def diameterOfBinaryTree(root):
    global diameter
    if not root:
        return 0

    l = diameterOfBinaryTree(root.left) #height of left subtree
    r = diameterOfBinaryTree(root.right) #heihgt of right subtree
    diameter = max(diameter, l+r) # cal the max diameter by adding both left and right heights

    return 1+max(l,r) #return the height to the parent

root = build_tree([1,2,3,4,5])
diameterOfBinaryTree(root)
print(diameter)