class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = [x for x in sorted(nums)[-k:]]
        heapq.heapify(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
            return self.minHeap[0]
        else:
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        
        return self.minHeap[0]
        

