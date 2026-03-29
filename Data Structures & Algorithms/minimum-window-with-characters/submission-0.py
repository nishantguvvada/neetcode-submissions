class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = {}
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1

        required_counts = len(target_counts)
        window_counts = {}
        formed = 0

        ans = float("inf"), None, None
        left, right = 0, 0
        while right < len(s):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in target_counts and window_counts[character] == target_counts[character]:
                formed += 1

            while left <= right and formed == required_counts:
                character = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_counts[character] -= 1
                if character in target_counts and window_counts[character] < target_counts[character]:
                    formed -= 1
                left += 1
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]