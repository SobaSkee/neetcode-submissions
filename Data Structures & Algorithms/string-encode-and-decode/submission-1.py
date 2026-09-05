class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            length = ""
            word = ""
            while s[index] != "#":
                length += s[index]
                index += 1
            
            for i in range(1, int(length)+1):
                word += s[index+i]
            res.append(word)
            index = index+int(length)+1
        return res
            


# e.g. "neet" -> "4#neet" read until the first hash that is the count
