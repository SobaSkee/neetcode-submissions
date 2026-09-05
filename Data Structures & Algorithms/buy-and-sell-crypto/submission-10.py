class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        resMax = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                resMax = max(resMax, prices[r]-prices[l])
        return resMax

