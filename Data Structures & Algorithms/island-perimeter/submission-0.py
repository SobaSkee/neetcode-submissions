class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = 0
        def check_edges(r,c):
            if r < 0 or r == rows or c < 0 or c == cols:
                return 0
            
            cur = 0
            for x, y in dirs:
                dx, dy = r+x, c+y
                if dx < 0 or dx == rows or dy < 0 or dy == cols:
                    cur += 1
                elif grid[dx][dy] == 0:
                    cur += 1
            
            return cur

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += check_edges(r, c)

        return res