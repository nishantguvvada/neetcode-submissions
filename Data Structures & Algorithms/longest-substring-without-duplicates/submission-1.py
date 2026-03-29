class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longest_len = 0
        store = set()

        while i < len(s):
            while s[i] in store:
                store.remove(s[j])
                j += 1
            store.add(s[i])
            longest_len = max(longest_len, i - j + 1)
            i += 1
        return longest_len