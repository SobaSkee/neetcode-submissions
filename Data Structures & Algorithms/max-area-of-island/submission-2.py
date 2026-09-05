class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        res = 0
        def getArea(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0:
                return 0
            area = 1
            grid[r][c] = 0
            for d in dirs:
                dr = r+d[0]
                dc = c+d[1]
                area += getArea(dr, dc)

            return area 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, getArea(r,c))
        return res
                




