class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for u, v, w in edges:
            if u in adj:
                adj[u].append([w,v])
            else:
                adj[u] = [[w, v]]

        shortest = {}
        minHeap = [[0, src]]
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in shortest:
                continue
            shortest[v1] = w1

            for w2, v2 in adj.get(v1, []):
                if v2 not in shortest:
                    heapq.heappush(minHeap, [w2+w1, v2])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest






        
