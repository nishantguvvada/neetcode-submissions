class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        m = len(nums) // 2
        if target > nums[m]:
            res = self.search(nums[m+1:], target)
            return m + 1 + res if res != -1 else -1
        elif target < nums[m]:
            return self.search(nums[:m], target)
        else:
            return m
