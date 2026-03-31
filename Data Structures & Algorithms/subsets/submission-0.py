class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(self, i):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(self, i + 1)
            subset.pop()
            dfs(self, i + 1)
        dfs(self, 0)
        return res
        

