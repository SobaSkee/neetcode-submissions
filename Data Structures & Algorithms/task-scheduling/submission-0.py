class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count freqs:
        freqs = Counter(tasks)
        heap = [-freq for freq in freqs.values()]
        heapq.heapify(heap)
        # queue stores (task, time task finishes)
        cooldown = deque()
        time = 0
        while heap or cooldown:
            time+=1
            if heap:
                freq = 1 + heapq.heappop(heap)
                if freq != 0:
                    cooldown.append((freq, time+n))
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])

        return time




# X - 1, Y - 2, nothing - 3, X - 4, Y - 5
# 5 cpu cycles