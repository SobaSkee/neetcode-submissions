class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 0
            if(i == len(temperatures)):
                result.append(count)
                break
            j = i+1
            greaterFound = False
            while j < len(temperatures):
                if temperatures[j] <= temperatures[i]:
                    count += 1
                else:
                    greaterFound = True
                    count += 1
                    break
                j += 1
            if greaterFound == True:
                result.append(count)
            else:
                result.append(0)
        return result