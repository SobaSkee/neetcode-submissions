class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            warmerFound = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    warmerFound = True
                    break
            if not warmerFound:
                res.append(0)
        return res
        # [22, 21, 20, 23, 25, 20]
            