class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW , COL = len(board), len(board[0])
        path = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            #invalid: out-of-bound, not word char, already seen/visited
            if (r < 0 or r >= ROW or c < 0 or c >= COL
                or word[i] != board[r][c] or (r,c) in path):
                return False
            
            #selec the path
            path.add((r,c))

            #explore all direction
            if backtrack(r + 1, c, i + 1): return True
            if backtrack(r - 1, c, i + 1): return True
            if backtrack(r, c + 1, i + 1): return True
            if backtrack(r, c - 1, i + 1): return True

            path.remove((r,c))
            return False
        
        for r in range(ROW):
            for c in range(COL):
                if backtrack(r, c, 0):
                    return True

        return False                
