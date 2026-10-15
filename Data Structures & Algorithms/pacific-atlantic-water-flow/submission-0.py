class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        pac = [[False]*cols for _ in range(rows)]
        atl = [[False]*cols for _ in range(rows)]

        pacific = []
        atlantic = []

        def bfs(source, ocean):
            q = collections.deque(source)
            while q:
                row, col = q.popleft()
                ocean[row][col] = True
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                        heights[nr][nc] >= heights[row][col] and 
                        not ocean[nr][nc]):
                        q.append((nr, nc))

        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))
        
        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
            
        return res