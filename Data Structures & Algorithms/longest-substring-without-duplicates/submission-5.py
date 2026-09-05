class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        dupes = set()

        for r in range(len(s)):
            while s[r] in dupes:
                dupes.remove(s[l])
                l += 1
            dupes.add(s[r])
            maxLen = max(maxLen, r-l+1)
        return maxLen