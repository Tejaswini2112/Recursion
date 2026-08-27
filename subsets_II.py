def subsetsWithDup(nums):
        res = []
        nums.sort()
        def fun_subsets(idx, curr):
            if idx>=len(nums):
                res.append(list(curr))
                return
            curr.append(nums[idx])
            fun_subsets(idx+1, curr)
            ele = curr.pop()
            next_idx = idx+1
            while next_idx<len(nums) and ele==nums[next_idx]:
                next_idx+=1
            fun_subsets(next_idx, curr)

        fun_subsets(0, [])
        return res

print(subsetsWithDup([1,2,2]))

# Difference between subsets, subarray and subsequence

# Term	                Order matters?	       Gaps allowed?	        How you generate/solve
# Subarray / substring	yes (contiguous)	   no — must be adjacent	sliding window, two pointers, prefix sum
# Subsequence	        yes (preserve order)   yes	                    include/exclude recursion
# Subset	            no (unordered)	       yes	                    include/exclude recursion (dedup if input has dups)