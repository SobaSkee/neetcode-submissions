class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindow = 0
        duplicates = set()
        l = 0
        for r in range(len(s)):
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l += 1
            duplicates.add(s[r])

            maxWindow = max(maxWindow, r-l+1)
        return maxWindow

    # z x y z
    #   l   r
    # 3 - 1 = 2