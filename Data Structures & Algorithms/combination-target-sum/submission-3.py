class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []
        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= n or total > target:
                return

            # choose to add
            subset.append(nums[i])
            dfs(i, subset, total + nums[i])
            subset.pop()

            # choose not to add
            dfs(i+1, subset, total)

        dfs(0, [], 0)
        return res