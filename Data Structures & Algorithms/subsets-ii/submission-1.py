class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            ## use the number
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            ## dont use the number
            while i < len(nums)-1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res

        
        