class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n*(n+1)//2
        sum_nums = 0
        for i in nums:
            sum_nums += i
        return total - sum_nums