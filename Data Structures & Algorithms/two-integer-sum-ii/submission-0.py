class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        while p1 < len(numbers):

            for i in range(len(numbers)):
                if numbers[i] == numbers[p1]:
                    continue
                if numbers[i] + numbers[p1] == target:
                    return [p1+1, i+1]
            p1 += 1
                
            
