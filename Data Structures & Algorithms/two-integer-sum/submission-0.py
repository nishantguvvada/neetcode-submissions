class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, val in enumerate(nums):
            diff = target - nums[i]
            if diff in store:
                return [store[diff], i]
            store[nums[i]] = i

