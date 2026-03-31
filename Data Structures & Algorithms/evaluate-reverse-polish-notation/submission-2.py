class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                right = stack.pop()
                left = stack.pop()
                if tokens[i] == "+":
                    stack.append(left + right)
                elif tokens[i] == "-":
                    stack.append(left - right)
                elif tokens[i] == "/":
                    stack.append(int(left / right))
                elif tokens[i] == "*":
                    stack.append(left * right)
                

        return stack[-1]