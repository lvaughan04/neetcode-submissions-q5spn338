class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        res_s = {}
        res_t = {}
        for i in range(len(s)):
            if s[i] in res_s:
                res_s[s[i]] += 1
            else:
                res_s[s[i]] = 1
            if t[i] in res_t:
                res_t[t[i]] += 1
            else:
                res_t[t[i]] = 1
        
        return res_s == res_t


        