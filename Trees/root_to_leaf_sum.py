# calculate current sum at each node on the path to form the number, once you reach the leaf node you now you got the number of that path
# add the left and right paths fo rtotal sums of the path
# TC-O(n), SC-O(h)
from tree_utils import build_tree

def sumNumbers(root):
    def rootToLeafSum(root, currSum):
        if not root:
            return 0
        # after reaching the leaf node, return the number of that path
        if not root.left and not root.right:
            return currSum*10+root.val
        l = rootToLeafSum(root.left, currSum*10+root.val) #currSum is the number formed so far, returns the sum of this path
        r = rootToLeafSum(root.right, currSum*10+root.val)
        return l+r #total sum of all the paths
        

    return rootToLeafSum(root, 0)

root = build_tree([4,9,0,5,1])
print(sumNumbers(root))