class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob2 = max(nums[0], nums[1])
        rob1 = nums[0]
        #[rob1, rob2, n, n + 1]
        for i in range(2, len(nums)):
            ## can either take the current num and rob1 or just take rob2, and then take the maximum of that
            tmp = rob2
            rob2 = max(rob1 + nums[i], rob2)
            rob1 = tmp
        return rob2