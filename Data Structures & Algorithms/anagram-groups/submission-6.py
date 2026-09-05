class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            anagrams[tuple(key)] = anagrams.get(tuple(key), []) + [s]
        return list(anagrams.values())

    # 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0