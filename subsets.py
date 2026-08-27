def subsets(nums):
        res = []
        def fun_subsets(idx, curr):
            if idx>=len(nums):
                res.append(list(curr))
                return
            curr.append(nums[idx])
            fun_subsets(idx+1, curr)
            curr.pop()
            fun_subsets(idx+1, curr)

        fun_subsets(0, [])
        return res

print(subsets([1,2,3,4,5]))