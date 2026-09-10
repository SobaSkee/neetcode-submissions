class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            if preMap[node] == []:
                return True
            visit.add(node)
            for pre in preMap[node]:
                if not dfs(pre): return False
            visit.remove(node)
            preMap[node] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        



        
