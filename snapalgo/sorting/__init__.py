#################################### Bubble sort #############################
def bubble_sort(nums):
    
    for x in range(len(nums)):
        for y in range(len(nums)-x-1):
            if nums[y] > nums[y+1]:
                nums[y],nums[y+1] = nums[y+1],nums[y]
                
    return nums

#################################### Bubble sort #############################


#################################### Insertion sort #############################
def insertion_sort(nums):
    
    for x in range(1,len(nums)): ## O(N)
        elem = nums[x]
        
        y = x-1
        
        while y>=0 and elem < nums[y]: ## O(N)
            nums[y+1] = nums[y]
            y-=1
            
        nums[y+1] = elem
        
        
    return nums

#################################### Insertion sort #############################


#################################### Merge sort #############################
def merge_sort(nums):
    
    if len(nums) > 1:
        mid = len(nums) // 2 ##split array from middle
        
        left_arr = nums[0:mid] 
        right_arr = nums[mid:] 
        
        merge_sort(left_arr)##sort left subarray
        merge_sort(right_arr)##sort right subarray
        
        i = 0
        j = 0
        k = 0
        ##merge the two sorted arrays in linear time to get a combined sorted array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                nums[k] = left_arr[i]
                i+=1
                
            else:
                nums[k] = right_arr[j]
                j+=1
                
                
            k+=1
                
        while i < len(left_arr):
            nums[k] = left_arr[i]
            i+=1
            k+=1
            
        while j < len(right_arr):
            nums[k] = right_arr[j]
            j+=1
            k+=1
            
        return nums

#################################### Merge sort #############################

#################################### Radix sort #############################

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

#################################### Radix sort #############################
