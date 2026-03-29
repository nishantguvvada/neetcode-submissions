class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        store = {}
        longest_len = 0
        max_freq = 0
        while right < len(s):
            store[s[right]] = store.get(s[right], 0) + 1
            max_freq = max(max_freq, store[s[right]])
            curr_len = right - left + 1
            while k < curr_len - max_freq:
                store[s[left]] -= 1
                left += 1
                curr_len = right - left + 1
            longest_len = max(longest_len, curr_len)
            right += 1
        return longest_len