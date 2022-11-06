def bubble_sort(nums):
    
    for x in range(len(nums)):
        for y in range(len(nums)-x-1):
            if nums[y] > nums[y+1]:
                nums[y],nums[y+1] = nums[y+1],nums[y]
                
    return nums