#solution - backtracking
#partition at each index and check if the first part is a palindrome, if it is a palindrome then perform recursion on the rest of the string
#TC - O(n*2^n), SC - O(n)
def partition(s):
    res = []
    # checking palindrome
    def is_palindrome(s, start, end):
        while(start<=end):
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    
    def func_partition(idx, path):
        # if we are at the end of the string that means we found the right partitions so record and return
        if idx >= len(s):
            res.append(list(path))
            return

        # loop through the entire array to partition at each index
        for i in range(idx, len(s)):
            # if the current partition is a palindrome add it to the path and perform recursion on the next part
            if is_palindrome(s, idx, i):  #check the partition from idx(start index) till i(pivot/partition index)
                path.append(s[idx:i+1]) #add to the path
                func_partition(i+1, path) #recursion for rest of the string
                path.pop() # remove the last string while backtracking
        
    func_partition(0, [])
    return res
