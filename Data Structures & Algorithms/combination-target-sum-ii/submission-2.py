class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []

        candidates.sort()

        def dfs(i, cur, total):
            # base cases
            if total == target:
                res.append(cur[::])
                return
            if total > target or i == n:
                return

            # include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()

            # skip candidates[i]
            # loop until the next adj is different 
            # so we dont have duplicate subsets
            # edge case:[1,1,1,1,1] so i+1<n
            while i+1< n and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res
