class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes = set()
        l = 0

        maxLen = 0
        for r in range(len(s)):
            while s[r] in dupes:
                dupes.remove(s[l])
                l += 1
            dupes.add(s[r])
            if (r-l+1) > maxLen:
                maxLen = (r-l+1)
        return maxLen
