class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROW, COL = len(board), len(board[0])

        def dfs(r, c , i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= ROW or c < 0 or c >= COL or board[r][c] != word[i] or
                (r,c) in path):
                return False
            
            path.add((r,c))

            if dfs(r + 1, c, i + 1): return True
            if dfs(r - 1, c, i + 1): return True
            if dfs(r, c + 1, i + 1): return True
            if dfs(r, c - 1, i + 1): return True

            path.remove((r,c))
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        
        return False
        