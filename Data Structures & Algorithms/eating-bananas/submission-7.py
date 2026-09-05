class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            totalTime = sum(math.ceil(pile/k) for pile in piles)
            if totalTime > h:
                l = k+1
            else:
                r = k-1
                res = k
        return res