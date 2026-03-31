class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        res = 1
        # [1, 2, 4, 3]
        for i in range(len(nums) - 1, -1, -1):
            ## starting at the end
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
                    res = max(res, lis[i])
        return res