class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet stores all seen courses along the current DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                # loop detected - course cannot be completed
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

