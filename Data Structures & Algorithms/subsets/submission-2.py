class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []

        def backtrack(i):

            # base case
            if i == n:
                res.append(subset.copy())
                return
            
            # dont pick nums[i]
            backtrack(i+1)
            subset.append(nums[i])

            # pick nums[i]
            backtrack(i+1)
            subset.pop()

        backtrack(0)

        return res