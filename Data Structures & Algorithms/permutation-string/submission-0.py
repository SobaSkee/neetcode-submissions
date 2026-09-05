class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freqs = Counter(s1)
        window = Counter()

        k = len(s1)

       
        for i, ch in enumerate(s2):
            window[ch] += 1

            if i >= k:
                old_char = s2[i-k]
                window[old_char] -= 1
                if window[old_char] == 0:
                    del window[old_char]
            if i >= k - 1 and window == s1_freqs:
                return True

        return False
