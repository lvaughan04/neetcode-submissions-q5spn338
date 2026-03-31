class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        count = {')': '(', '}' : '{', ']': '['}

        for char in s:
            if char in count.values():
                stack.append(char)
            else:
                if stack:
                    if stack.pop() != count[char]:
                        return False
                else:
                    return False
        
        return len(stack) == 0