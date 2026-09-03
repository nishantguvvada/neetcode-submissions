class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # s = sorted(s)
        # t = sorted(t)
        # l, r = 0, 0
        # while l < len(s):
        #     if s[l] != t[r]:
        #         return False
        #     l += 1
        #     r += 1
        # return True
        return sorted(s) == sorted(t)