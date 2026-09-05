class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l = 1
        r = max(piles)
        res = r # worst case
        while l <= r:
            k = (l+r)//2
            totalTime = sum(math.ceil(pile/k) for pile in piles)
            if totalTime > h:
                l = k+1
            # decrease k, update res to be the new best time
            else:
                r = k-1
                res = k
        return res

