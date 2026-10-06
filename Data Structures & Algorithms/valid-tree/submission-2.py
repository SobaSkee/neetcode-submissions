class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree contains no cycles
        # n-1 edges

        # if node has indegree > 1 then not valid
        if len(edges) != n-1:
            return False
        
        graph = [[] for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return False
            
            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        dfs(0)
        return len(seen) == n
