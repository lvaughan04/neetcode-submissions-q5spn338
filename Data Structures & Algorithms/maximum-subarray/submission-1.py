class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        
        while left < len(nums):
            curr = nums[left]
            right = left + 1
            res = max(res, nums[left])
            while right < len(nums) and curr > 0:
                curr += nums[right]
                right += 1
                res = max(res, curr)
            left += 1
        return res
        

        ## essentiall the whole idea is that when encountering a positive number compare it against the sum so far and then keep adding next sums
        ## until you reach a negative sum or reach the end of the array