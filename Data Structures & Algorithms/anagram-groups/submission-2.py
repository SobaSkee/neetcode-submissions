class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []
        for word in strs:
            wordSorted = "".join(sorted(word))
            if wordSorted not in anagrams:
                groups = []
                anagrams[wordSorted] = groups
                anagrams[wordSorted].append(word)
            else:
                anagrams[wordSorted].append(word)
        for values in anagrams.values():
            res.append(values)
        return res