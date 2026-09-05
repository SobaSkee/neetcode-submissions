class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        s1Freq = Counter(s1)
        window = Counter()
        for r, ch in enumerate(s2):
            window[ch] += 1

            if r-l+1 > len(s1):
                window[s2[l]] -= 1
                l += 1

            if window == s1Freq:
                return True
        return False