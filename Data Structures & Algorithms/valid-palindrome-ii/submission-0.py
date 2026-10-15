class Solution:
    def validPalindrome(self, s: str) -> bool:

        stack = [c for c in s]
        i = 0
        allowed = 1
        while stack:
            curr = stack.pop()
            print(curr)
            if curr != s[i]:
                skip_left = s[i + 1:len(stack) + 1]
                skip_right = s[i:len(stack)]

                return (
                    skip_left == skip_left[::-1]
                    or skip_right == skip_right[::-1]
                )
            i += 1
        return True
