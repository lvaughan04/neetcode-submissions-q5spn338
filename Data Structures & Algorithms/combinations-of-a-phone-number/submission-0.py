class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        count = {"2" : "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def dfs(currentWord, i):
            if i == len(digits):
                res.append(currentWord)
                return
            
            ## take it and then undo
            letters = count[digits[i]]
            for char in letters:
                currentWord += char
                dfs(currentWord, i + 1)
                currentWord = currentWord[:-1]
        dfs("", 0)
        return res