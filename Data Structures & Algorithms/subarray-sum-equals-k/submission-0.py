class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        count[0] = 1
        prefixSum = 0
        for num in nums:
            prefixSum += num
            if prefixSum - k in count:
                res += count[prefixSum-k]
            count[prefixSum] += 1
        
        return res