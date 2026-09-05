class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        dupes = set()
        l = 0

        for r in range(len(s)):
            while s[r] in dupes:
                dupes.remove(s[l])
                l += 1
            
            dupes.add(s[r])
            res = max(res, r-l+1)
        return res