class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = {}
        
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        return max(counts, key=counts.get)