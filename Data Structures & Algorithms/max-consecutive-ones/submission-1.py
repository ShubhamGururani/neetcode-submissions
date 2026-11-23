class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        current = 0
        if nums[0]==1:
            current =1
        for i in range(1, len(nums)):
            if nums[i]==1:
                current+=1
            else:
                ans = max(current,ans)
                current = 0
        ans = max(current, ans)
        return ans
                
        