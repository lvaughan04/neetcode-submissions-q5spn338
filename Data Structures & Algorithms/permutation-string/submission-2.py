class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2:
            return False
    
        countOne = [0] * 26 ## for 26 letters
        countTwo = [0] * 26 ## for 26 letters

        for i in range(n1):
            countOne[ord(s1[i]) - ord("a")] += 1
            countTwo[ord(s2[i]) - ord("a")] += 1

        
        if countOne == countTwo:
            return True

        ## if you dont start at this, it essentially is an index out of bounds
        ## since you try to remove a character from the window but the window wasnt set
        ## in the second array
        for i in range(n1, n2):
            countTwo[ord(s2[i]) - ord("a")] += 1 ##add next character in window
            countTwo[ord(s2[i-n1]) - ord("a")] -= 1 ## remove character from window
            if countOne == countTwo:
                return True
        
        return False
