class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            sLen = int(s[i:j])

            word = s[j+1:j+1+sLen]
            res.append(word)
            i = j + 1 + sLen
        return res

