class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s) < len(t):
            return ""
        
        ## the start of a substring is when a character in s is in T and ends when all characters in T exist
        tCount = Counter(t)
        window = {}

        have, need = 0, len(tCount)
        resLength = 1001
        res = ""
        left = 0
        for r in range(len(s)):  
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1
            while have == need:
                ## update the window
                if r - left + 1 < resLength:
                    resLength = r - left + 1
                    res = s[left: r + 1]
                
                ## pop left from the window
                window[s[left]] -= 1
                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1
        return res
        