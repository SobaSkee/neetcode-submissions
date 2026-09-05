class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        maxLen = 0

        l = 0
        for r in range(len(s)):
            charDict[s[r]] = 1 + charDict.get(s[r], 0)
            while (r-l+1) - max(charDict.values()) > k:
                charDict[s[l]] -= 1
                l += 1
            maxLen = max(maxLen,(r-l)+ 1)

        return maxLen



# dupes = {X}
# maxLen
# XYYX, k=2
# X l=0 | r=0, k=2, maxLen=1
# XY -> XX | l=0, r=1, k=1, maxLen=2
# XXY -> XXX | l=0, r=2, k=0, maxLen=3
# XXXX | maxLen=4