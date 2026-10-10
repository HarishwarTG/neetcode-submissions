class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(openC, closeC):
            if openC == closeC == n:
                res.append("".join(path))
                return
            
            if openC < n:
                path.append("(")
                backtrack(openC + 1, closeC)
                path.pop()
            
            if closeC < openC:
                path.append(")")
                backtrack(openC, closeC + 1)
                path.pop()
            
        backtrack(0, 0)
        return res
            
            
