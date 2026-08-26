# time complexity - O(n*(2^n))  ->  2^n for all the subsequences, n for creating copying each list everytime in the base condition
# space - O(n)
res = []
def print_subsequences(idx, arr, curr):

    #if we are reaching the end of the array record the result and return
    if idx>=len(arr):
        res.append(list(curr)) #create a copy of curr to avoid referencing to the same list everytime any modifications are mase to the curr
        return
    
    #choose the current index
    curr.append(arr[idx])  
    print_subsequences(idx+1, arr, curr)

    #not choose the current index
    curr.pop()  
    print_subsequences(idx+1, arr, curr)

print_subsequences(0, [3,1,2], [])
print(res)