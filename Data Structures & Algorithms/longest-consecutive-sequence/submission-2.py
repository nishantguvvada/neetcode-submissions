class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        store = set(nums)
        longest = 1
        for idx, val in enumerate(nums):
            seq_len = 1
            if val - 1 not in store:
                current_num = val
                
                while current_num + 1 in store:
                    current_num += 1
                    seq_len += 1
            longest = max(longest, seq_len)
        return longest