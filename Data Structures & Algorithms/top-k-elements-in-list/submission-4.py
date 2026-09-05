class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)
        res = []
        for num in nums:
            numsDict[num] += 1
        
        frequencies = numsDict.values()
        for i in range(k):
            maxFreq = max(frequencies)
            for key in numsDict:
                if numsDict[key] == maxFreq:
                    res.append(key)
                    del numsDict[key]
                    break


        return res