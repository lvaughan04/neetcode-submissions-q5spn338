class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumVal = 0
        count = defaultdict(int)
        count[0] = 1
        res = 0

        for num in nums:
            sumVal += num
            if sumVal - k in count:
                res += count[sumVal - k]
            count[sumVal] += 1
        
        return res