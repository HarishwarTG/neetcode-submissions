class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            q = collections.deque([(r,c)])
            board[r][c] = "S"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                        board[nr][nc] == "O"):
                        board[nr][nc] = "S"
                        q.append([nr, nc])

        for c in range(cols):
            if board[0][c] and board[0][c] == "O":
                bfs(0, c)
            if board[rows -1][c] and board[rows - 1][c] == "O":
                bfs(rows -1, c)

        for r in range(1, rows - 1):
            if board[r][0] and board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols - 1] and board[r][cols -1] == "O":
                bfs(r, cols -1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"