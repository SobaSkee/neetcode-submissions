class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        freqs = [[] for i in range(len(nums)+1)]

        for n, c in counts.items():
            freqs[c].append(n)
        
        for i in range(len(freqs)-1, 0, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res)==k:
                    return res