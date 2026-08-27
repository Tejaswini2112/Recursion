# calculate the left subsequences and right subsequences or choose and not choose calls 
# for whose sum equals to k
# if we are reaching the end of the array and the sum equals to k, that means we found a squence so return 1(this will add to the count), else 0

#Time Complexity - O(2^n), Space - O(n) - call stack
def count_subsequence_sum_k(idx, arr, k, s):
    if idx>=len(arr):
        if s == k:
            return 1
        return 0

    l = count_subsequence_sum_k(idx+1, arr, k, s+arr[idx]) # left recursion count or choose count
    r = count_subsequence_sum_k(idx+1, arr, k, s) # right recursion count or not choose count

    return l+r

print(count_subsequence_sum_k(0, [1,2,3,1], 3, 0))