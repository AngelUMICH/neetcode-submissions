class Solution:
    def isPalindrome(self, s: str) -> bool:
        # sanitize the string
        s_1 = "".join(c for c in s if c.isalnum()).lower()
        print(s_1)
        for a,b in zip(s_1, s_1[::-1]):
            if not a == b:
                return False
        return True