#swap the left and right sub trees and recurse
from tree_utils import build_tree

def invertTree(root):
    if root == None:
        return None

    # swapping left and right sub trees
    temp = root.left
    root.left = root.right
    root.right = temp
    # recurse on the left and right sub trees
    invertTree(root.left)
    invertTree(root.right)
    return root

root = build_tree([4,2,7,1,3,6,9])
print(invertTree(root))