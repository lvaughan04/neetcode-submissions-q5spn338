class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 100001
        left = 0
        right = 0
        count = 0
        ## 
        while right < len(nums):
            count += nums[right]
            while left <= right and count > target:
                res = min(res, right - left + 1)
                count -= nums[left]
                left += 1
            if count == target:
                res = min(res, right - left + 1)
            right += 1

        if res == 100001:
            return 0
        else:
            return res