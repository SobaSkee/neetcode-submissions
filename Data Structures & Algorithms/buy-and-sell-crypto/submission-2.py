class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxProfit = 0
        left = 0

        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
