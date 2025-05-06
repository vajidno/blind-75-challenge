# def max_subarray(nums):
#     max_sum = float('-inf')
 
#     for i in range(len(nums)):
#         curr_sum = 0
#         for j in range(len(nums)):
#             curr_sum += nums[j]
#             max_sum = max(curr_sum,max_sum)

#     return max_sum

def max_subarray(nums):
    curr_sum = max_sum =  nums[0]
    for i in range(1,len(nums)):
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum            



print(max_subarray([5,4,-1,7,8]))            

