class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        # [30, 38, 30, 36, 35, 50, 28]
        # [[38, 1], [30, 2], ]
        # [1, ]
        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i], i])
                continue
            while stack and stack[-1][0] < temperatures[i]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])
        return res
            
            