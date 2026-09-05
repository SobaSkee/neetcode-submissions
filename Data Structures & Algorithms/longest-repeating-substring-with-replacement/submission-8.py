class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        m = {}
        res = 0

        for r in range(len(s)):
            m[s[r]] = m.get(s[r], 0) + 1
            while (r-l+1) - max(m.values()) > k:
                m[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        return res
