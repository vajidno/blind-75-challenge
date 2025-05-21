nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    results = set()
    for i in range(len(nums)):
        seen = set()
        for j in range(i+1,len(nums)):
            complement = -(nums[i]+nums[j])
            if complement in seen:
                triplet = tuple(sorted((nums[i],nums[j],complement)))
                results.add(triplet)
            else:
                seen.add(nums[j])
            
    return [list(result) for result in results]



def ThreeSum(nums):
    result = []
    nums = sorted(nums)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result


print(ThreeSum(nums))
              

