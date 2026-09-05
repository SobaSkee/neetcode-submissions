class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Map = {chr(ord('a') + i): 0 for i in range(26)}
        s2Map = {chr(ord('a') + i): 0 for i in range(26)}

        for c in s1:
            s1Map[c] += 1
        for i in range(len(s1)):
            s2Map[s2[i]] += 1

        matches = 0
        for c in s1Map:
            if s1Map[c] == s2Map.get(c,0):
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # add right character
            c = s2[r]
            s2Map[c] += 1
            if s1Map[c] == s2Map[c]:
                matches += 1
            elif s1Map[c] + 1 == s2Map[c]:
                matches -= 1

            # remove left
            c = s2[l]
            s2Map[c] -= 1
            if s1Map[c] == s2Map[c]:
                matches += 1
            elif s1Map[c] - 1 == s2Map[c]:
                matches -= 1
            
            l += 1
        return matches == 26


            


