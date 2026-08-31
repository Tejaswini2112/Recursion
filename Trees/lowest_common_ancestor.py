#Approach - traverse the tree recursively, once a node is equal to either p or q nodes, that means we found atleat one value so return it and dont traverse further
# while traversing, if both the left and right node returns a node that means the current node is the common ancestor
# if only one side returns a node, just pass that to the parent
# TC - O(n), SC - O(h)
from tree_utils import build_tree

def lowestCommonAncestor(root, p, q):
    if root == None:
        return None

    # if the root value is equal to either p or q return the root node
    if root == p or root == q:
        return root
    
    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)

    if l and r: #if both left and right returns a node, that means current node is the lowest common ancestor for both
        return root
    elif l: #if only left tree returns a node, pass this node to the parent
        return l
    elif r: #same for right node
        return r

def find_node(root, value):
    if root is None:
        return None
    if root.val == value:
        return root
    return find_node(root.left, value) or find_node(root.right, value)

root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
p = find_node(root, 5)
q = find_node(root, 1)
print(lowestCommonAncestor(root, p, q).val)