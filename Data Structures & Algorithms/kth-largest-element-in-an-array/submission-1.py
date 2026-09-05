class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappush(minHeap, num)
                heapq.heappop(minHeap)
        return minHeap[0]
        