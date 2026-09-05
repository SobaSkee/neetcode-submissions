class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        q = deque()
        
        def visitCell(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == -1:
                return
            q.append([r,c])
            visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # gate
                    q.append([r, c])
                    visited.add((r,c))
        dist = 0
        while q:
    
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                visitCell(r+1,c)
                visitCell(r-1,c)
                visitCell(r,c+1)
                visitCell(r,c-1)

            dist += 1

