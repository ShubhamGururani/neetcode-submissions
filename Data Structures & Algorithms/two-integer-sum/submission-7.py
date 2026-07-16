class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        hash_map = dict()
        for j in range(len(nums)):
            hash_map[nums[j]] = j
        # print(hash_map)
        for j in range(len(nums)):
            req = target - nums[j]
            if hash_map.get(req) and hash_map.get(req)!=j:
                return [j, hash_map[req]]
        return [-1,-1]