nums = [11,13,15,17]
def findMinSortedRotatedArray(nums):
    count = 0
    n = len(nums)
    for i in range(len(nums)):
        if nums[i]>nums[(i+1)%n]:
            count+=1
            min = nums[i+1]
    return count==1,min       

def find_min_sorted_rotated_array(nums):
    res = nums[0]
    left = 0
    right = len(nums)-1
    while left<=right:
        if nums[left]<nums[right]:
            res = min(res,nums[left])
            break
        mid = (left+right)//2
        res = min(res,nums[mid])
        if nums[left] <= nums[mid]:
            left = mid+1
        else:
            right = mid-1
    return res

print(find_min_sorted_rotated_array([2,1]))            
