class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for bracket in s:
            if bracket not in close:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != close[bracket]:
                    return False
        
        if stack:
            return False
        else:
            return True