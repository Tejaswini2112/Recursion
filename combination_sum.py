#TC - 2^(m+n)*n (m+n because its not just 2 decisions for each idx, we are incrementingly considering the same index until it becomes equal to the target)
#SC = n*x (x = no.of combinations)

#Explanation- keep considering the same index until sum is equal to or greater than the target
#next also donot consider the same index to check other combinations

def combinationSum(candidates, target):
    res = []

    def combinations(idx, s, curr):
        # if the sum is equal to the target record the result and return
        if s == target:
            res.append(list(curr))
            return
        # if idx goes out of bounds or sum becomes greater than the target return
        if idx >= len(candidates) or s > target:  
            return

        #choose the same index
        curr.append(candidates[idx])
        combinations(idx, s + candidates[idx], curr)

        #do not the same index, pop and move forward to the next index
        curr.pop()
        combinations(idx + 1, s, curr)

    combinations(0, 0, [])
    return res

print(combinationSum([2,3,6,7], 7))