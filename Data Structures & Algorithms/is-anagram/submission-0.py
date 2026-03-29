class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        store_s = {}
        store_t = {}
        for i in range(len(s)):
            store_s[s[i]] = store_s.get(s[i], 0) + 1
            store_t[t[i]] = store_t.get(t[i], 0) + 1
        
        return store_s == store_t
