class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for s in strs:
            sortedS = ''.join(sorted(s))

            anagrams[sortedS] = anagrams.get(sortedS, []) + [s]
        return list(anagrams.values())