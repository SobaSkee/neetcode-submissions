class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        resMax = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                resMax = max(resMax, profit)
        return resMax