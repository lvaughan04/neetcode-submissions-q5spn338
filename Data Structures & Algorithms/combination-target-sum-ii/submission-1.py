class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        def backtrack(start, currentSum, subset):
            if currentSum > target:
                return
            elif currentSum == target:
                ## add the array to the results variable
                res.append(subset[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(i + 1, currentSum + candidates[i], subset)
                subset.pop()
        backtrack(0, 0, [])
        return res