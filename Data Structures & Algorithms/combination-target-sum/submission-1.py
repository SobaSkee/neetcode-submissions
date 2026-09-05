class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, cur, total):

            # first base case
            if total == target:
                res.append(cur.copy())
                return
            
            # second base case
            if i >= len(nums) or total > target:
                return

            # pick number
            cur.append(nums[i])
            dfs(i, cur, total+nums[i])
            cur.pop()

            # dont pick number
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res






