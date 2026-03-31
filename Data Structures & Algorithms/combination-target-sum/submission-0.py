class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr, subset):
            if curr == target:
                res.append(subset[:])
                return
            elif curr > target or i == len(nums):
                return

            backtrack(i+1, curr, subset)
            
            subset.append(nums[i])
            backtrack(i, curr + nums[i], subset)
            subset.pop()
         

        backtrack(0, 0, [])
        return res