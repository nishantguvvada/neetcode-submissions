class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_var = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_var = max(max_var, count)
            else:
                count = 0
        return max_var