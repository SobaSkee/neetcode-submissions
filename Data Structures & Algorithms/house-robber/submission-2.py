class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        if len(nums) < 3:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            first = dp[i-2]
            second = dp[i-1]
            dp[i] = max(first+nums[i], second)
        print(dp)
        return dp[-1]

# test run
# reg=[2, 1, 1, 2]
# dp= [2, 1, 3, 3]
# i = 2, first=2, second=9, dp[2]=10
# i = 3, first=9, second=8, dp[3]=12
# i = 4, first=, second=

            
            
            