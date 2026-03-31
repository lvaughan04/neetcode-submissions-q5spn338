class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        count = set()

        for num in nums:
            count.add(num)
        
        for num in nums:
            if num - 1 not in count:
                length = 1
                while num + 1 in count:
                    num += 1
                    length += 1
                res = max(res, length)
        return res

