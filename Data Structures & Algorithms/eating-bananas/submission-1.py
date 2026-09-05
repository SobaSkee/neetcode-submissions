class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)
        bestSpeed = maxSpeed
        while minSpeed <= maxSpeed:
            mid = (minSpeed + maxSpeed) // 2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / mid)
            if totalHours <= h:
                bestSpeed = mid
                maxSpeed = mid - 1
            elif totalHours > h:
                minSpeed = mid + 1


            
        return bestSpeed

            
            


# minSpeed = 1, maxSpeed = 4
# mid = 2
        