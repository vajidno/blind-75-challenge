def maxProduct(nums):
    max_product = min_product = 1
    result = nums[0]
    for num in nums:
        temp = max_product*num
        max_product = max(temp,min_product*num,num)
        min_product = min(temp,min_product*num,num)
        result = max(result,max_product)
    return result    
print(maxProduct([2,3,-2,4]))
