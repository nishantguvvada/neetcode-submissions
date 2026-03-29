class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        # return s == s[::-1]
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True