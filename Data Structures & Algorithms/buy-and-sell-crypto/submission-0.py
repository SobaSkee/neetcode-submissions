class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxSum = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                if profit > maxSum:
                    maxSum = profit
            right += 1
        return maxSum
                
            