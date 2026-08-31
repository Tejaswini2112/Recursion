#divide the tree into left and right sub trees, now compare the outer child of left and right sub trees and inner childs of left anf right sub tree, they should be equal to be symmetric
#TC-O(n), SC-O(h)
from tree_utils import build_tree

def isSymmetric(root):
    def isMirror(leftTree, rightTree):
        if not leftTree and not rightTree:
            return True
        if not leftTree or not rightTree:
            return False

        # compare the left values of left tree with the right values of right sub tree and vice versa
        return leftTree.val == rightTree.val and isMirror(leftTree.left, rightTree.right) and isMirror(leftTree.right, rightTree.left)
    
    return isMirror(root.left, root.right)

root = build_tree([1,2,2,3,4,4,3])
print(isSymmetric(root))