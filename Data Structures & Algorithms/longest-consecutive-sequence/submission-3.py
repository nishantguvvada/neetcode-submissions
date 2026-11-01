class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        count = 0
        max_count = 0
        for n in store:
            if n - 1 not in store:
                count = 1
                curr = n + 1
                while curr in store:
                    count += 1
                    curr += 1
                max_count = max(max_count, count)
        return max_count