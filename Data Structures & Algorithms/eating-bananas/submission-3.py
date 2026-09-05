class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slowest = 1
        fastest = max(piles)
        res = fastest

        while slowest <= fastest:
            mid = (slowest + fastest) // 2
            totalTime = 0
            for x in piles:
                totalTime += 1 if x <= mid else math.ceil(x / mid) 
            
            if totalTime > h:
                slowest = mid + 1
            else:
                res = mid
                fastest = mid - 1
        return res
            

#0, 1, 2, 3, 4

# x <= k -> h = 1
# x > k -> h = ceil(x / k)