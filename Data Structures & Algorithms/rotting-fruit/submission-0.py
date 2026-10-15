class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # visit = set()
        minutes = 0
        fresh = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, minutes))
                elif grid[r][c] == 1:
                    fresh += 1
                    # visit.add((r, c))
        
        while q:
            row, col, time = q.popleft()
            minutes = max(minutes, time)
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    q.append((nr, nc, time + 1))
                    fresh -= 1
                    # visit.add((r,c))
            
        return minutes if fresh == 0 else -1