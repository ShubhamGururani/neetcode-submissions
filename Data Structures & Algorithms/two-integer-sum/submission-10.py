class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) -1
        diff = {}
        for i in range(len(nums)):
            current_req = target - nums[i]
            diff[current_req] = i
        for i in range(len(nums)):
            current = nums[i]
            if diff.get(current) and diff.get(current)!=i:
                return [i, diff[current]]
            
        return [-1,-1]
        
            
