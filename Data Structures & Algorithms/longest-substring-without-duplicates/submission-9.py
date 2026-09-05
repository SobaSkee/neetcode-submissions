class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # contains all unique chars for the curr valid substring window
        subStrSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in subStrSet:
                subStrSet.remove(s[l])
                l += 1
            subStrSet.add(s[r])
            res = max(res, r-l+1)
        return res
