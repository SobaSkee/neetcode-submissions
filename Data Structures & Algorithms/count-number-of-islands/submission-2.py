class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque([])
        dirs = [(-1,0), (0, 1), (1,0), (0,-1)]
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    res += 1
                    q.append((r,c))
                    visit.add((r,c))

                    while q:
                        cur = q.popleft()
                        for d in dirs:
                            dx = d[0]+cur[0]
                            dy = d[1]+cur[1]
                            if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visit and grid[dx][dy] == '1':
                                q.append((dx, dy))
                                visit.add((dx, dy))

        return res


                    

        
