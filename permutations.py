# TC - O(n*n!) n for copying path and n! for permutations
# SC - O(n) stack space (depth of the recursion tree)
def permute(nums):
    res = []
    used = [False]*len(nums)

    def permutation(path, used):
        # when the path length is equal to the nums length, we achieved one combination, so record it
        if len(path) == len(nums):
            res.append(list(path))
            return

        # loop through the entire array for all possible elements at every position
        # maintain used list to mark the element thats already in the path
        for i in range(len(nums)):
            # only add an element to the path if it is not in the path or used and mark it as used by setting it to true
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                # perform permutations on the leftover elements
                permutation(path, used) # call the function itself for the next elements/combinations to add to the path
                path.pop() # undo while backtracking to keep the path clean
                used[i] = False #mark used as false after undoing
    
    permutation([], used)
    return res

print(permute([1,2,3]))