class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0