class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()

        left = 0
        right = 0
        res = 0
        while left < len(s) and right < len(s):
            while left <= right and s[right] in count:
                count.remove(s[left])
                left += 1
            count.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        
        return res
                
            