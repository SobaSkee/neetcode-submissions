class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupes = set()
        maxLen = 0

        l = 0

        for r in range(len(s)):
            while s[r] in dupes:
                dupes.remove(s[l])
                l += 1

            dupes.add(s[r])
            maxLen = max(r-l+1, maxLen)
        return maxLen