class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        index = [False] * len(nums)
        def backtrack(subset, visited):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for i in range(len(nums)):
                num = nums[i]
                if visited[i]:
                    continue
                subset.append(num)
                visited[i] = True
                backtrack(subset, visited)
                subset.pop()
                visited[i] = False

        backtrack([], index)
        return res

            