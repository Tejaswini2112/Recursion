#TC - O(n*(2^n))
#SC - O(n)

res=[]
def subsequence_sum_k(idx, arr, k, curr, s):

    if idx>=len(arr):
        # when the index reaches the end compare the sum only then add to result
        if s == k:
            res.append(list(curr))
        return

    #consider current index
    curr.append(arr[idx])
    subsequence_sum_k(idx+1, arr, k, curr, s+arr[idx]) # add current element to the sum, to maintain the sum so far

    #do not consider current index
    curr.pop()
    subsequence_sum_k(idx+1, arr, k, curr, s)


subsequence_sum_k(0, [1,3,2,1], 3, [], 0)
print(res)
