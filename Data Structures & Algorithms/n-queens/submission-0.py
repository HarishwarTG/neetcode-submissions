class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set() 
        posDia = set() # r + c
        negDia = set() # r - c 

        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(r) for r in board])
                return
            
            for c in range(n):
                if c in col or (r + c) in posDia or (r - c) in negDia:
                    continue
                
                col.add(c)
                posDia.add(r + c)
                negDia.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDia.remove(r + c)
                negDia.remove(r - c)
                board[r][c] = "."
            
        backtrack(0)
        return res