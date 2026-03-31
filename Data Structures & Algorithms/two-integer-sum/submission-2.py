class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = []
        seen = {}
        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if seen.get(diff) != None:
                return [seen[diff], i]
            else:
                ## add the index
                seen[nums[i]] = i
                i += 1