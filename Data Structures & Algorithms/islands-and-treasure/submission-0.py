class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        N = len(grid)
        M = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def minDist(r, c, dist):
            if r < 0 or r >= N or c < 0 or c >= M:
                return
            if grid[r][c] == -1 or grid[r][c] < dist:
                return

            grid[r][c] = dist
            for dr, dc in dirs:
                minDist(r + dr, c + dc, dist + 1)
        
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    minDist(r, c, 0)
        
            