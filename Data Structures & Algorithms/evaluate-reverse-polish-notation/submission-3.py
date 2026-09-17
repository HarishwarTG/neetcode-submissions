class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(t)
            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                if t == "+":
                    stack.append(val1 + val2)
                elif t == "-":
                    stack.append(val1 - val2)
                elif t == "/":
                    stack.append(val1 / val2)
                else:
                    stack.append(val1 * val2)
        
        return int(stack[-1])
        