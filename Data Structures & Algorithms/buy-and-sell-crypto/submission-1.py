class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxProfit = 0
        left = 0  # Buy day

        for right in range(1, len(prices)):  # Sell day
            if prices[right] < prices[left]:
                left = right  # Found a better buying day
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)

        return maxProfit
                
            