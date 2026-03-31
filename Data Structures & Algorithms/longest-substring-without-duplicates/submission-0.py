class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## have a hashmap that you add characters to when you
        ## loop through the array
        ## key condition if the next character is already in the array
        ## then you have to move the left pointer one spot and then check again


        result = set()
        left , right = 0, 0
        answer = 0

        while (right < len(s)):
            ##key condition
            while (s[right] in result):
                result.remove(s[left])
                left += 1
            result.add(s[right])
            right += 1
            answer = max(answer, right - left)

        return answer
            