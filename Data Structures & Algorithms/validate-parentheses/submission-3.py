class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if stack:
                    value = stack.pop()
                    if value != pairs[char]:
                        return False
                else:
                    return False
        
        return len(stack) == 0