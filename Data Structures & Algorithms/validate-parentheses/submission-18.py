class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # mapping = {'}':'{', ']':'[', ')':'('}
        mapping = {'{':'}', '[':']', '(':')'}

        for c in s:
            if c in mapping:
                stack.append(c)
            elif c in mapping.values():
                if stack and c == mapping[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0