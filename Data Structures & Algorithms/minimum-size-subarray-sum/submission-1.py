class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float('inf')

        l = 0 
        curr_sum = 0
        for r in range(len(nums)):
            
            curr_sum += nums[r]

            while curr_sum >= target:

                shortest = min(shortest, r-l+1)
                curr_sum -= nums[l]
                l += 1
        if shortest == float('inf'):
            return 0
            
        return shortest
            