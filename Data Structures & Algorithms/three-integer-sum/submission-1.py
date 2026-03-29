class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        store = []
        for idx, val in enumerate(sorted_nums):
            if idx > 0 and sorted_nums[idx] == sorted_nums[idx-1]:
                continue
            left = idx + 1
            right = len(sorted_nums) - 1

            while left < right:
                if sorted_nums[left] + sorted_nums[right] < -1*val:
                    left += 1
                elif sorted_nums[left] + sorted_nums[right] > -1*val:
                    right -= 1
                else:
                    store.append([val, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
        return store
