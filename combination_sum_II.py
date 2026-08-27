#same as subsequence sum k but with a twist, avoid duplicates
#TC - O(n*(2^n)), SC - O(n)
def combinationSum2(candidates, target):
    #sort initially as the result should be sorted
    candidates.sort()
    result = []
    def combination(idx, s, curr):
        if s == target:
            result.append(list(curr))
            return
        if idx>=len(candidates) or s>target:
            return

        curr.append(candidates[idx])
        combination(idx+1, s+candidates[idx], curr)
        ele = curr.pop()
        next_idx = idx+1

        # avoid duplicates by not selecting the next element same as the last element
        while next_idx<len(candidates) and ele==candidates[next_idx]:
            next_idx+=1 #keep incrementing the index until a new element is found

        combination(next_idx, s, curr)
        
    combination(0, 0, [])
    return result

print(combinationSum2([10,1,2,7,6,1,5], 8))
