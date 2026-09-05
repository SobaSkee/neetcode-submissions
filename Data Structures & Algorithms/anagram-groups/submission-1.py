class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        anagrams = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in anagrams:
                anagrams[sortedS] = []
            
            anagrams[sortedS].append(s)
        
        return anagrams.values()
       