class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        #adjaceny list
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for s, d, weight in edges:
            adj[s].append([d, weight])

        shortest = {} # map vertex to distance of shortest path from source

        # dijkstra's is a greedy bfs algorithm:
        # starting at src and bfs until calculate shortest distance
        minHeap = [[0, src]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2, in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w2+w1, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest




        