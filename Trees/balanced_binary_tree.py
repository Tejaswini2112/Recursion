#Recursive Approach
#Find the heights of both left and right sub trees and check the difference, if the diff is >1 that means it is not a balanced b tree, else it is balanced
#Very similar to max depth of binary tree problem
#TC - O(n), SC - O(n)
from tree_utils import build_tree

def balancedTree(root):
    if root == None:
        return 0
    # check height of left sub tree
    l = balancedTree(root.left)
    if l == -1: #-1 means the tree is unbalanced, so just return -1 without further execution
        return -1
    r = balancedTree(root.right)
    if r==-1:
        return -1

    if abs(l-r) >1: #if the diff btw left and right trees is more than 1 it is unbalanced tree
        return -1
    
    return 1+max(l,r) # this will get executed only when the tree is balanced so far

root = build_tree([1,2,2,3,3,None,None,4,4])
if balancedTree(root)==-1:
    print(False)
else:
    print(True)

