class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        minutes = 0
        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    dx = r + dr
                    dy = c + dc
                    if 0 <= dx < ROWS and 0 <= dy < COLS and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        fresh -= 1
                        q.append([dx,dy])
            minutes += 1
        return minutes if fresh == 0 else -1

