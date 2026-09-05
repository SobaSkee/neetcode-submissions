class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for char in s:
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1
        for char in t:
            if char not in tMap:
                tMap[char] = 1
            else:
                tMap[char] += 1    
        return (sMap == tMap)