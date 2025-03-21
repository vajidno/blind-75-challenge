class Solution:
    def two_sum(self,arr:list[int],target:int)->list[int]:
        prev_map = dict()
        for i in range(len(arr)):
            sec_num = target - arr[i]
            if sec_num in prev_map:
                return [i,prev_map[sec_num]]
            else:
                prev_map[arr[i]]=i
        return []

sol = Solution()
print(sol.two_sum([2,7,11,15],9)) 

