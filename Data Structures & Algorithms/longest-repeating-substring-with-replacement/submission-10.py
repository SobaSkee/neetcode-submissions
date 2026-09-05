class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        dupes = {}
        l = 0
        res = 0

        for r in range(len(s)):
            dupes[s[r]] = dupes.get(s[r], 0) + 1
            while (r-l+1) - max(dupes.values()) > k:
                dupes[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
        return res