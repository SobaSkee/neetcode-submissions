class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []

        candidates.sort()

        def dfs(start, total, subset):
            # base cases
            if total == 0:
                res.append(subset.copy())
                return 
            if total < 0:
                return

            for i in range(start, n):
                # skip duplicate numbers 
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, total-candidates[i], subset+[candidates[i]])
        dfs(0, target, [])
        return res
