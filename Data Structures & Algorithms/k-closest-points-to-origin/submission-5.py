class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for xi, yi in points:
            dist = math.sqrt(xi**2 + yi**2)
            if len(maxHeap) == k:
                if -maxHeap[0][0] > dist:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-dist, xi, yi))
            else:
                heapq.heappush(maxHeap, (-dist, xi, yi))
        res = []
        for _, xi, yi in maxHeap:
            res.append([xi, yi])
        return res



