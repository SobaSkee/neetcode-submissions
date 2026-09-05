class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()

        stack = []
        for c in cleaned:
            stack.append(c)
        
        for c in cleaned:
            top = stack.pop()
            print(f"comparing {c} to {top}")
            if c != top:
                return False
        return True