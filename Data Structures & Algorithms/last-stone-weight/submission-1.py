class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            print(x, y)

            newWeight = y-x
            heapq.heappush(maxHeap, -newWeight)
            print(maxHeap)
        
        if len(maxHeap) == 1:
            return -maxHeap[0]
        else:
            return 0