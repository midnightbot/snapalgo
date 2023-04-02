def flatten(B):##O(B)
    nums = []
    for x in range(len(B)):
        for y in range(len(B[x])):
            nums.append(B[x][y])
            
    return nums
def radix_sort(nums,max_digits):##O(MAX_DIGTIS * (N+B))
    
    for digit in range(0,max_digits): ##O(MAX_DIGITS)
        B = [[] for x in range(10)]
        
        for item in nums:##O(N)
            thisdigit = item // 10 ** digit%10
            B[thisdigit].append(item)
            
            
        nums = flatten(B)##O(B)
        
    return nums