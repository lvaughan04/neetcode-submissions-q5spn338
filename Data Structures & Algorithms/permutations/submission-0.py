class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, visited):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for num in nums:
                if num in visited:
                    continue
                subset.append(num)
                visited.add(num)
                backtrack(subset, visited)
                subset.pop()
                visited.remove(num)

        backtrack([], set())
        return res

            